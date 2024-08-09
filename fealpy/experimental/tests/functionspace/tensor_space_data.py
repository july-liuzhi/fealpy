import numpy as np
from fealpy.decorator import cartesian
from fealpy.experimental.backend import backend_manager as bm
triangle_mesh = [
        {
            ##input
            "triangle_mesh":np.array([2,2],dtype=np.int32),


            ##result
            "tdofnumel":2,
            "GD":1,
            "ld":3,
            "tcell2dof":np.array([[ 3, 12,  4, 13,  0,  9],
                                [ 6, 15,  7, 16,  3, 12],
                                [ 4, 13,  5, 14,  1, 10],
                                [ 7, 16,  8, 17,  4, 13],
                                [ 1, 10,  0,  9,  4, 13],
                                [ 4, 13,  3, 12,  7, 16],
                                [ 2, 11,  1, 10,  5, 14],
                                [ 5, 14,  4, 13,  8, 17]], dtype=np.int32),
            
            "tphi": 
             np.array([[[[0.6666667, 0.0000000],
                      [0.1666667, 0.0000000],
                      [0.1666667, 0.0000000],
                      [0.0000000, 0.6666667],
                      [0.0000000, 0.1666667],
                      [0.0000000, 0.1666667]],

                     [[0.1666667, 0.0000000],
                      [0.6666667, 0.0000000],
                      [0.1666667, 0.0000000],
                      [0.0000000, 0.1666667],
                      [0.0000000, 0.6666667],
                      [0.0000000, 0.1666667]],

                     [[0.1666667, 0.0000000],
                      [0.1666667, 0.0000000],
                      [0.6666667, 0.0000000],
                      [0.0000000, 0.1666667],
                      [0.0000000, 0.1666667],
                      [0.0000000, 0.6666667]]]], dtype=np.float64),
            "tface2dof": np.array([[ 1, 10,  0,  9],
                                [ 0,  9,  3, 12],
                                [ 4, 13,  0,  9],
                                [ 2, 11,  1, 10],
                                [ 1, 10,  4, 13],
                                [ 5, 14,  1, 10],
                                [ 5, 14,  2, 11],
                                [ 3, 12,  4, 13],
                                [ 3, 12,  6, 15],
                                [ 7, 16,  3, 12],
                                [ 4, 13,  5, 14],
                                [ 4, 13,  7, 16],
                                [ 8, 17,  4, 13],
                                [ 8, 17,  5, 14],
                                [ 6, 15,  7, 16],
                                [ 7, 16,  8, 17]], dtype=np.int32),

   
            "tgrad_phi": np.array([[[[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]]],



        [[[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]]],



        [[[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]]],



        [[[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]],


         [[[ 2., -2.],
           [ 0., -0.]],

          [[ 0.,  2.],
           [ 0.,  0.]],

          [[-2.,  0.],
           [-0.,  0.]],

          [[ 0., -0.],
           [ 2., -2.]],

          [[ 0.,  0.],
           [ 0.,  2.]],

          [[-0.,  0.],
           [-2.,  0.]]]],



        [[[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]]],



        [[[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]]],



        [[[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]]],



        [[[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]],


         [[[-2.,  2.],
           [-0.,  0.]],

          [[ 0., -2.],
           [ 0., -0.]],

          [[ 2.,  0.],
           [ 0.,  0.]],

          [[-0.,  0.],
           [-2.,  2.]],

          [[ 0., -0.],
           [ 0., -2.]],

          [[ 0.,  0.],
           [ 2.,  0.]]]]], dtype=np.float64),

        }

        ]