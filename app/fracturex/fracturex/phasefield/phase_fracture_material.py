import numpy as np
from typing import Optional

from fealpy.typing import TensorLike
from fealpy.backend import backend_manager as bm
from fealpy.material.elastic_material import LinearElasticMaterial

from fealpy.decorator import barycentric

class BasedPhaseFractureMaterial(LinearElasticMaterial):
    def __init__(self, material, energy_degradation_fun):
        """
        Parameters
        ----------
        material : 材料参数
        """
        self._gd = energy_degradation_fun # 能量退化函数
        if 'lam' in material and 'mu' in material:
            self.lam = material['lam']
            self.mu = material['mu']
        elif 'E' in material and 'nu' in material:
            self.E = material['E']
            self.nu = material['nu']

            self.lam = self.E * self.nu / ((1 + self.nu) * (1 - 2 * self.nu))
            self.mu = self.E / (2 * (1 + self.nu))
        else:
            raise ValueError("The material parameters are not correct.")


        self._uh = None
        self._d = None

        self.H = None # 谱分解模型下的最大历史场

    def update_disp(self, uh):
        self._uh = uh

    def update_phase(self, d):
        self._d = d

    def update_historical_field(self, H):
        self.H = H

    @ barycentric
    def effective_stress(self, bc=None) -> TensorLike:
        """
        Compute the effective stress tensor, which is the stress tensor without the damage effect.

        Parameters
        ----------
        u : TensorLike
            The displacement field.
        strain : TensorLike 
            The strain tensor.
        Returns
        -------
        TensorLike
            The effective stress tensor.
        """
        strain = self.strain_value(bc)

        lam = self.lam
        mu = self.mu
        trace_e = np.trace(strain, axis1=-2, axis2=-1)
        I = bm.eye(strain.shape[-1])
        stress = lam * trace_e[..., None, None] * I + 2 * mu * strain
        return stress

    @ barycentric
    def strain_value(self, bc=None) -> TensorLike:
        """
        Compute the strain tensor.
        """ 
#        if bc is None:
#            bc = bm.array([1/3, 1/3, 1/3], dtype=bm.float64)
        uh = self._uh
        guh = uh.grad_value(bc)
        
        strain = 0.5 * (guh + bm.swapaxes(guh, -2, -1))
        return strain
    
    @ barycentric
    def linear_elastic_matrix(self, bc=None) -> TensorLike:
        """
        Compute the linear elastic matrix.
        """
        strain = self.strain_value(bc)

        GD = strain.shape[-1]
       
        lam = self.lam
        mu = self.mu
        if GD == 2:
            D0 = bm.tensor([[lam + 2 * mu, lam, 0],
                          [lam, lam + 2 * mu, 0],
                          [0, 0, mu]], dtype=bm.float64)
        elif GD == 3:
            D0 = bm.tensor([[lam + 2 * mu, lam, lam, 0, 0, 0],
                            [lam, lam + 2 * mu, lam, 0, 0, 0],
                            [lam, lam, lam + 2 * mu, 0, 0, 0],
                            [0, 0, 0, mu, 0, 0],
                            [0, 0, 0, 0, mu, 0],
                            [0, 0, 0, 0, 0, mu]], dtype=bm.float64)
        else:
            raise NotImplementedError("This dim is not correct, we cannot give the linear elastic matrix.")
        return D0


class IsotropicModel(BasedPhaseFractureMaterial):
    @ barycentric
    def stress_value(self, bc) -> TensorLike:
        """
        Compute the fracture stress tensor.
        """
        d = self._d

        gd = self._gd.degradation_function(d(bc)) # 能量退化函数 (NC, NQ)
        stress = self.effective_stress(bc) * gd[..., None, None]
        return stress

    @ barycentric
    def elastic_matrix(self, bc) -> TensorLike: 
        """
        Compute the tangent matrix.
        """
        d = self._d
        gd = self._gd.degradation_function(d(bc)) # 能量退化函数 (NC, NQ)
        D0 = self.linear_elastic_matrix(bc=bc) # 线弹性矩阵
        D = D0 * gd[..., None, None]
        return D
    
       

class AnisotropicModel(BasedPhaseFractureMaterial):
    def stress_value(self, bc) -> TensorLike:
        # 计算各向异性模型下的应力
        pass

    def elastic_matrix(self, bc) -> TensorLike: 
        # 计算各向异性模型下的切线刚度矩阵
        pass

class DeviatoricModel(BasedPhaseFractureMaterial):
    def stress_value(self, bc) -> TensorLike:
        # 计算偏应力模型下的应力
        pass

    def elastic_matrix(self, bc) -> TensorLike: 
        # 计算偏应力模型下的切线刚度矩阵
        pass


class SpectralModel(BasedPhaseFractureMaterial):
    def stress_value(self, bc) -> TensorLike:
        # 计算谱分解模型下的应力
        pass

    def elastic_matrix(self, bc) -> TensorLike: 
        # 计算谱分解模型下的切线刚度矩阵
        pass

    def strain_energy_density_decomposition(self, s: TensorLike):
        """
        @brief Strain energy density decomposition from Miehe Spectral
        decomposition method.
        @param[in] s strain，（NC, NQ, GD, GD）
        """

        lam = self.lam
        mu = self.mu

        # 应变正负分解
        sp, sm = self.strain_pm_eig_decomposition(s)

        _ts = np.trace(s, axis1=-2, axis2=-1)
        ts = bm.array(_ts, dtype=bm.float64)

        tp, tm = self.macaulay_operation(ts)
        tsp = np.trace(sp**2, axis1=-2, axis2=-1)
        tsm = np.trace(sm**2, axis1=-2, axis2=-1)

        phi_p = lam * tp ** 2 / 2.0 + mu * tsp
        phi_m = lam * tm ** 2 / 2.0 + mu * tsm
        return phi_p, phi_m

    def strain_pm_eig_decomposition(self, s: TensorLike):
        """
        @brief Decomposition of Positive and Negative Characteristics of Strain.
        varespilon_{\pm} = \sum_{a=0}^{GD-1} <varespilon_a>_{\pm} n_a \otimes n_a
        varespilon_a is the a-th eigenvalue of strain tensor.
        n_a is the a-th eigenvector of strain tensor.
        
        @param[in] s strain，（NC, NQ, GD, GD）
        """
        w, v = bm.linalg.eigh(s) # w 特征值, v 特征向量
        p, m = self.macaulay_operation(w)

        sp = bm.zeros_like(s)
        sm = bm.zeros_like(s)
        
        GD = s.shape[-1]
        for i in range(GD):
            n0 = v[..., i]  # (NC, NQ, GD)
            n1 = p[..., i, None] * n0  # (NC, NQ, GD)
            sp += n1[..., None] * n0[..., None, :]

            n1 = m[..., i, None] * n0
            sm += n1[..., None] * n0[..., None, :]
        return sp, sm

    
    def macaulay_operation(self, alpha):
        """
        @brief Macaulay operation
        """
        val = bm.abs(alpha)
        p = (alpha + val) / 2.0
        m = (alpha - val) / 2.0
        return p, m

    def heaviside(self, x):
        """
        @brief
        """
        val = bm.zeros_like(x)
        val[x > 1e-13] = 1
        val[bm.abs(x) < 1e-13] = 0.5
        val[x < -1e-13] = 0
        return val
    
    @ barycentric
    def maximum_historical_field(self, bc):

        """
        @brief Maximum historical field
        """
        strain = self.strain_value(bc)
       
        phip, _ = self.strain_energy_density_decomposition(strain)
        
        if self.H is None:
            self.H = phip[:]
        else:
            self.H = np.fmax(self.H, phip)
        return self.H
        

class HybridModel(BasedPhaseFractureMaterial):
    def __init__(self, material, energy_degradation_fun):
        """
        Parameters
        ----------
        material : 材料参数
        """
        
        self._isotropic_model = IsotropicModel(material, energy_degradation_fun)
        self._spectral_model = SpectralModel(material, energy_degradation_fun)
        super().__init__(material, energy_degradation_fun)

    @ barycentric
    def stress_value(self, bc) -> TensorLike:
        """
        Compute the fracture stress tensor.
        """
        self._isotropic_model._uh = self._uh
        self._isotropic_model._d = self._d
        return self._isotropic_model.stress_value(bc=bc)

    @ barycentric
    def elastic_matrix(self, bc) -> TensorLike: 
        self._isotropic_model._uh = self._uh
        self._isotropic_model._d = self._d
        
        return self._isotropic_model.elastic_matrix(bc=bc)

    @ barycentric
    def maximum_historical_field(self, bc):
        """
        @brief Maximum historical field
        """
        self._spectral_model._uh = self._uh
        self._spectral_model._d = self._d
        self._spectral_model.H = self.H
        
        self.H = self._spectral_model.maximum_historical_field(bc)
        return self.H
        

class PhaseFractureMaterialFactory:
    """
    工厂类，用于创建不同的本构模型
    """
    @staticmethod
    def create(model_type, material, energy_degradation_fun):
        """
        Parameters
        ----------
        model_type : str
            本构模型类型
        material : dict
        """
        if model_type == 'IsotropicModel':
            return IsotropicModel(material, energy_degradation_fun)
        elif model_type == 'AnisotropicModel':
            return AnisotropicModel(material, energy_degradation_fun)
        elif model_type == 'SpectralModel':
            return SpectralModel(material, energy_degradation_fun) 
        elif model_type == 'DeviatoricModel':
            return DeviatoricModel(material, energy_degradation_fun)
        elif model_type == 'HybridModel':
            return HybridModel(material, energy_degradation_fun)
        else:
            raise ValueError(f"Unknown model type: {model_type}")