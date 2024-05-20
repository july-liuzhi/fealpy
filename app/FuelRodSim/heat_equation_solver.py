import numpy as np
import os
from scipy.sparse.linalg import spsolve
from fealpy.mesh import TriangleMesh,TetrahedronMesh
from fealpy.functionspace import LagrangeFESpace
from fealpy.fem import DiffusionIntegrator, BilinearForm, ScalarMassIntegrator, LinearForm, ScalarSourceIntegrator
from fealpy.fem.dirichlet_bc import DirichletBC
import matplotlib.pyplot as plt

class FuelRod3dData:
    def domain(self):
        return [0, 1, 0, 1, 0, 1]

    def duration(self):
        return [0, 1]

    def source(self,p,t):
        return 0

    def dirichlet(self, p, t):
        return np.array([500])
    
class HeatEquationSolver:
    def __init__(self, mesh: TriangleMesh, pde: FuelRod3dData, nt, bdnidx, p0, alpha_caldding=4e-4, alpha_inner=8e-4, layered=True, ficdx=None ,cacidx=None,output: str = './result', filename: str = 'temp'):
        """
        Args:
            mesh (TriangleMesh): 三角形网格
            pde (ParabolicData): 双曲方程的数据
            nt (_type_): 时间迭代步长
            bdnidx (_type_): 边界条件，布尔值or索引编号
            p0 (_type_): 初始温度
            layered (bool, optional):刚度矩阵分层. Defaults to True.
            output (str, optional): 生成文件的名字. Defaults to './result'.
            filename (str, optional): Defaults to 'temp'.
        """
        self.mesh = mesh
        self.pde = pde
        self.bdnidx = bdnidx
        self.layered = layered
        self.output = output
        self.filename = filename
        self.space = LagrangeFESpace(mesh, p=1)
        self.GD = self.space.geo_dimension()
        self.duration = pde.duration()
        self.nt = nt
        self.p0 = p0
        self.ficdx=ficdx
        self.cacidx=cacidx
        self.tau = (self.duration[1] - self.duration[0]) / self.nt
        self.alpha_caldding = alpha_caldding
        self.alpha_inner = alpha_inner
        self.initialize_output_directory()
        self.threshold = self.create_threshold()

    def initialize_output_directory(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)

    def create_threshold(self):
        """
        可以分辨布尔数组和编号索引，如果是布尔数组直接传入，如果是索引编号转换为布尔数组
        """
        if isinstance(self.bdnidx, np.ndarray) and self.bdnidx.dtype == bool:
            return self.bdnidx
        else:
            NN = len(self.mesh.entity('node'))
            isbdnidx = np.full(NN, False, dtype=bool)
            isbdnidx[self.bdnidx] = True
            return isbdnidx


    def solve(self):
        self.p = self.space.function()
        self.p += self.p0  
        for n in range(self.nt):
            t = self.duration[0] + n * self.tau
            bform3 = LinearForm(self.space)
            # 这里应该传入后的得到的为qc
            #f=self.pde.source(node,t)
            source=lambda p: self.pde.source(p, t)
            print(source)
            bform3.add_domain_integrator(ScalarSourceIntegrator(source, q=3))
            self.F = bform3.assembly()
            
            # 组装刚度矩阵
            NC = self.mesh.number_of_cells()
            alpha = np.zeros(NC)
        
            if self.layered:
                # 假设 ficdx 和 cacidx 是定义好的两个索引列表
                # 默认分层
                alpha[self.ficdx] += self.alpha_inner
                alpha[self.cacidx] += self.alpha_caldding
            else:
                # 如果不分层，使用统一的 alpha_caldding
                alpha += self.alpha_caldding

            bform = BilinearForm(self.space)
            bform.add_domain_integrator(DiffusionIntegrator(alpha, q=3))
            self.K = bform.assembly()

            # 组装质量矩阵
            bform2 = BilinearForm(self.space)
            bform2.add_domain_integrator(ScalarMassIntegrator(q=3))
            self.M = bform2.assembly()
            A = self.M + self.alpha_caldding * self.K * self.tau
            b = self.M @ self.p + self.tau * self.F
            if n == 0:
                A = A
                b = b
            else:
                gD=lambda x : self.pde.dirichlet(x,t)
                ipoints = self.space.interpolation_points()
                gD=gD(ipoints[self.threshold])
                bc = DirichletBC(space=self.space, gD=gD.reshape(-1,1), threshold=self.threshold)
                A, b = bc.apply(A, b)
                self.p = spsolve(A, b)
            print(self.p)
            self.mesh.nodedata['temp'] = self.p.flatten('F')
            name = os.path.join(self.output, f'{self.filename}_{n:010}.vtu')
            self.mesh.to_vtk(fname=name)
        print('self.p',self.p)
        print(self.p.shape)
        
    def plot_exact_solution(self):
        t = self.duration[1]
        exact_solution = self.pde.solution(self.mesh.node, t)
        print('exact_solution',exact_solution)

        if self.GD == 2:
            plt.figure(figsize=(8, 6))
            plt.scatter(self.mesh.node[:, 0], self.mesh.node[:, 1], c=exact_solution, cmap='viridis', s=10)
            plt.colorbar()
            plt.title('Exact Solution Scatter Plot')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.tight_layout()
            plt.show()
        elif self.GD == 3:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(self.mesh.node[:, 0], self.mesh.node[:, 1], self.mesh.node[:, 2], c=exact_solution, cmap='viridis', s=10)
            plt.colorbar(ax.collections[0], ax=ax)
            ax.set_title('Exact Solution Scatter Plot')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            plt.tight_layout()
            plt.show()

    def plot_error(self):
        t = self.duration[1]
        exact_solution = self.pde.solution(self.mesh.node, t)
        numerical_solution = self.p.flatten('F')
        error = np.abs(exact_solution - numerical_solution)
        print('error',error)

        if self.GD == 2:
            plt.figure(figsize=(8, 6))
            plt.scatter(self.mesh.node[:, 0], self.mesh.node[:, 1], c=error, cmap='viridis', s=10)
            plt.colorbar()
            plt.title('Error Scatter Plot')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.tight_layout()
            plt.show()
        elif self.GD == 3:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(self.mesh.node[:, 0], self.mesh.node[:, 1], self.mesh.node[:, 2], c=error, cmap='viridis', s=10)
            plt.colorbar(ax.collections[0], ax=ax)
            ax.set_title('Error Scatter Plot')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            plt.tight_layout()
            plt.show()


