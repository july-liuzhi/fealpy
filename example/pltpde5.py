import numpy as np
import matplotlib.pyplot as plt
import time

from fealpy.pde.darcy_forchheimer_2d import DeltaData
from fealpy.pde.darcy_forchheimer_2d import Example11
from fealpy.pde.darcy_forchheimer_2d import Example12
from fealpy.pde.darcy_forchheimer_2d import Example13
from fealpy.pde.darcy_forchheimer_2d import Example14
from fealpy.fdm.forchheimer import Dforchheimer
#from fealpy.fdm.velocity import NonDarcyForchheimerFDMModel
#from fealpy.fdm.DarcyForchheimerFDMModel_pu import DarcyForchheimerFDMModel
#from fealpy.fdm.DarcyForchheimerFDMModelpu import DarcyForchheimerFDMModel
#from fealpy.fdm.testDarcyForchheimerFDMModelpu import DarcyForchheimerFDMModel

box = [0,1,0,1]
mu = 2
k = 1
rho = 1
beta = 5
tol = 1e-6
#hx = np.array([0.12,0.34,0.22,0.32])
#hy = np.array([0.25,0.13,0.33,0.29])
#hy = np.array([0.16,0.23,0.32,0.11,0.18])
hx = np.array([0.25,0.25,0.25,0.25])
hy = np.array([0.25,0.25,0.25,0.25])
#hy = np.array([0.2,0.2,0.2,0.2,0.2])
m = 8
hx = hx/m
hy = hy/m
hx = hx.repeat(m)
hy = hy.repeat(m)

#pde = DeltaData(box,mu,k,rho,beta,tol)
pde = Example11(box,mu,k,rho,beta,tol)
#pde = Example12(box,mu,k,rho,beta,tol)
#pde = Example13(box,mu,k,rho,beta,tol)
#pde = Example14(box,mu,k,rho,beta,tol)
t1 = time.time()
mesh = pde.init_mesh(hx,hy)
fdm = Dforchheimer(pde,mesh)
np.set_printoptions(threshold = 1e6)
count,uh = fdm.solve()
nx = hx.shape[0]
ny = hy.shape[0]
X,Y = np.meshgrid(np.arange(0,1,hx[0]),np.arange(0,1,hy[0]))
isYDEdge = mesh.ds.y_direction_edge_flag()
u = uh[:sum(isYDEdge)]
print(uh.shape)
print(u.shape)
U = u.reshape(ny,nx+1)
v = uh[sum(isYDEdge):]
V = v.reshape(ny+1,nx)
plt.figure()
Q = plt.quiver(X,Y,U,0)
W = plt.quiver(X,Y,0,V)
plt.show()
