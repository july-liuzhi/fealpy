import numpy as np
import argparse

from fealpy.backend import backend_manager as bm
from fealpy.mesh import TriangleMesh, QuadrangleMesh


from app.fracturex.fracturex.phasefield.main_solver import MainSolver
from fealpy.utils import timer
import time
import matplotlib.pyplot as plt

class square_with_circular_notch():
    def __init__(self):
        """
        @brief 初始化模型参数
        """
        E = 210
        nu = 0.3
        Gc = 2.7e-3
        l0 = 0.03
        self.params = {'E': E, 'nu': nu, 'Gc': Gc, 'l0': l0}

    def is_y_force(self):
        """
        @brief 位移增量条件
        Notes
        -----
        这里向量的第 i 个值表示第 i 个时间步的位移的大小
        """
        return bm.concatenate((bm.linspace(0, 5e-3, 501), bm.linspace(5e-3,
            5.9e-3, 901)[1:]))
    
    def is_x_force(self):
        """
        @brief x 方向的力
        """
        return bm.linspace(0, 2.2e-2, 2201)

    def is_force_boundary(self, p):
        """
        @brief 标记位移增量的边界点
        """
        isDNode = bm.abs(p[..., 1] - 1) < 1e-12 
        return isDNode

    def is_dirchlet_boundary(self, p):
        """
        @brief 标记边界条件
        """
        return bm.abs(p[..., 1]) < 1e-12
    

    def adaptive_mesh(self, mesh, d0=0.49, d1=1.01, h=0.005):
        cell = mesh.entity("cell")
        node = mesh.entity("node")
        isMarkedCell = mesh.entity_measure('cell') > 0.00001
        isMarkedCell = isMarkedCell & (bm.min(bm.abs(node[cell, 1] - 0.5),
                                          axis=-1) < h)
        isMarkedCell = isMarkedCell & (bm.min(node[cell, 0], axis=-1) > d0) & (
            bm.min(node[cell, 0], axis=-1) < d1)
        return isMarkedCell

## 参数解析
parser = argparse.ArgumentParser(description=
        """
        脆性断裂任意次自适应有限元
        """)

parser.add_argument('--degree',
        default=1, type=int,
        help='Lagrange 有限元空间的次数, 默认为 1 次.')

parser.add_argument('--maxit',
        default=30, type=int,
        help='最大迭代次数, 默认为 30 次.')

parser.add_argument('--backend',
        default='numpy', type=str,
        help='有限元计算后端, 默认为 numpy.')

parser.add_argument('--model_type',
        default='HybridModel', type=str,
        help='有限元方法, 默认为 HybridModel.')

parser.add_argument('--mesh_type',
        default='tri', type=str,
        help='网格类型, 默认为 tri.')

parser.add_argument('--enable_adaptive',
        default=False, type=bool,
        help='是否启用自适应加密, 默认为 False.')

parser.add_argument('--marking_strategy',
        default='recovery', type=str,
        help='标记策略, 默认为重构型后验误差估计.')

parser.add_argument('--refine_method',
        default='bisect', type=str,
        help='网格加密方法, 默认为 bisect.')

parser.add_argument('--n',
        default=6, type=int,
        help='初始网格加密次数, 默认为 6.')

parser.add_argument('--vtkname',
        default='test', type=str,
        help='vtk 文件名, 默认为 test.')

parser.add_argument('--save_vtkfile',
        default=True, type=bool,
        help='是否保存 vtk 文件, 默认为 False.')

args = parser.parse_args()
p= args.degree
maxit = args.maxit
backend = args.backend
model_type = args.model_type
enable_adaptive = args.enable_adaptive
marking_strategy = args.marking_strategy
refine_method = args.refine_method
n = args.n
save_vtkfile = args.save_vtkfile
vtkname = args.vtkname +'_' + args.mesh_type + '_'


tmr = timer()
next(tmr)
start = time.time()
bm.set_backend(backend)
model = square_with_circular_notch()

if args.mesh_type == 'tri':
    mesh = TriangleMesh.from_square_domain_with_fracture()

elif args.mesh_type == 'quad':
    mesh = QuadrangleMesh.from_square_domain_with_fracture()
else:
    raise ValueError('Invalid mesh type.')


mesh.uniform_refine(n=n)

'''
isMarkedCell = model.adaptive_mesh(mesh)
while isMarkedCell.any():
    mesh.bisect(isMarkedCell)
    isMarkedCell = model.adaptive_mesh(mesh)
'''
fname = args.mesh_type + '_square_with_a_notch_init.vtu'
mesh.to_vtk(fname=fname)


ms = MainSolver(mesh=mesh, material_params=model.params, p=p, model_type=model_type)
tmr.send('init')

if enable_adaptive:
    print('Enable adaptive refinement.')
    ms.set_adaptive_refinement(marking_strategy=marking_strategy, refine_method=refine_method)

# 拉伸模型边界条件
ms.add_boundary_condition('force', 'Dirichlet', model.is_force_boundary, model.is_y_force(), 'y')

# 剪切模型边界条件
#ms.add_boundary_condition('force', 'Dirichlet', model.is_force_boundary, model.is_x_force(), 'x')
#ms.add_boundary_condition('displacement', 'Dirichlet', model.is_force_boundary, 0, 'y')

# 固定位移边界条件
ms.add_boundary_condition('displacement', 'Dirichlet', model.is_dirchlet_boundary, 0)


ms.solve(maxit=maxit, save_vtkfile=save_vtkfile, vtkname=vtkname)

tmr.send('stop')
end = time.time()

force = ms.Rforce
disp = ms.force_value
tname = args.mesh_type + '_p' + str(p) + '_' + 'model1_disp.txt'
with open(tname, 'w') as file:
    file.write(f'force: {force},\n time: {end-start},\n degree:{p},\n, backend:{backend},\n, model_type:{model_type},\n, enable_adaptive:{enable_adaptive},\n, marking_strategy:{marking_strategy},\n, refine_method:{refine_method},\n, n:{n},\n, maxit:{maxit},\n, vtkname:{vtkname}\n')
fig, axs = plt.subplots()
plt.plot(disp, force, label='Force')
plt.xlabel('Displacement Increment')
plt.ylabel('Residual Force')
plt.title('Changes in Residual Force')
plt.grid(True)
plt.legend()
pname = args.mesh_type + '_p' + str(p) + '_' + 'model1_force.png'
plt.savefig(pname, dpi=300)

print(f"Time: {end - start}")
