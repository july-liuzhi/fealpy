import numpy as np

# 定义多个典型的 FirstNedelecDof2d 对象
# mesh = TriangleMesh.from_box(nx = 1,ny =1)
# p =  4
init_data = [
    {
        "edof":4,
        "cdof":12,
        "gdof":364,
        "cell2dof":np.array([[ 15,  14,  13,  12,  23,  22,  21,  20,  27,  26,  25,  24,  63,
         62,  61,  60,  67,  66,  65,  64,  75,  74,  73,  72, 280, 281,
        282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 208, 210, 209,
        213, 212, 211, 214, 216, 215, 219, 218, 217, 184, 185, 186, 187,
        188, 189, 190, 191, 192, 193, 194, 195, 172, 174, 173, 177, 176,
        175, 178, 180, 179, 183, 182, 181, 292, 293, 294, 295, 296, 297,
        298, 299, 300, 301, 302, 303],
       [ 19,  18,  17,  16,  15,  14,  13,  12,  27,  26,  25,  24,  59,
         58,  57,  56,  71,  70,  69,  68,  67,  66,  65,  64, 268, 269,
        270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 184, 185, 186,
        187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199,
        200, 201, 202, 203, 204, 205, 206, 207, 160, 162, 161, 165, 164,
        163, 166, 168, 167, 171, 170, 169, 304, 305, 306, 307, 308, 309,
        310, 311, 312, 313, 314, 315],
       [  3,   2,   1,   0,  19,  18,  17,  16,  27,  26,  25,  24,  35,
         34,  33,  32,  39,  38,  37,  36,  71,  70,  69,  68, 232, 233,
        234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 196, 197, 198,
        199, 200, 201, 202, 203, 204, 205, 206, 207, 100, 101, 102, 103,
        104, 105, 106, 107, 108, 109, 110, 111,  88,  90,  89,  93,  92,
         91,  94,  96,  95,  99,  98,  97, 316, 317, 318, 319, 320, 321,
        322, 323, 324, 325, 326, 327],
       [ 11,  10,   9,   8,   3,   2,   1,   0,  27,  26,  25,  24,  31,
         30,  29,  28,  55,  54,  53,  52,  39,  38,  37,  36, 220, 221,
        222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 100, 101, 102,
        103, 104, 105, 106, 107, 108, 109, 110, 111, 148, 149, 150, 151,
        152, 153, 154, 155, 156, 157, 158, 159,  76,  78,  77,  81,  80,
         79,  82,  84,  83,  87,  86,  85, 328, 329, 330, 331, 332, 333,
        334, 335, 336, 337, 338, 339],
       [  7,   6,   5,   4,  11,  10,   9,   8,  27,  26,  25,  24,  43,
         42,  41,  40,  51,  50,  49,  48,  55,  54,  53,  52, 244, 245,
        246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 148, 149, 150,
        151, 152, 153, 154, 155, 156, 157, 158, 159, 136, 137, 138, 139,
        140, 141, 142, 143, 144, 145, 146, 147, 112, 114, 113, 117, 116,
        115, 118, 120, 119, 123, 122, 121, 340, 341, 342, 343, 344, 345,
        346, 347, 348, 349, 350, 351],
       [ 23,  22,  21,  20,   7,   6,   5,   4,  27,  26,  25,  24,  47,
         46,  45,  44,  75,  74,  73,  72,  51,  50,  49,  48, 256, 257,
        258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 136, 137, 138,
        139, 140, 141, 142, 143, 144, 145, 146, 147, 208, 210, 209, 213,
        212, 211, 214, 216, 215, 219, 218, 217, 124, 126, 125, 129, 128,
        127, 130, 132, 131, 135, 134, 133, 352, 353, 354, 355, 356, 357,
        358, 359, 360, 361, 362, 363]]),

        "basis":np.array([[[[ 0.03, -0.01,  0.  ],
         [ 0.06, -0.02,  0.  ],
         [ 0.01,  0.01, -0.01],
         [ 0.01,  0.01, -0.01],
         [ 0.06,  0.  ,  0.01],
         [ 0.36,  0.  ,  0.06],
         [-0.02,  0.06, -0.04],
         [-0.01,  0.03, -0.02],
         [-0.12,  0.12,  0.04],
         [-0.36,  0.36,  0.12],
         [ 0.  , -0.06,  0.07],
         [ 0.  , -0.36,  0.42],
         [-0.06,  0.18, -0.12],
         [ 0.  , -0.12,  0.14],
         [ 0.06,  0.  ,  0.01],
         [ 0.  ,  0.06, -0.07],
         [ 0.18, -0.06,  0.  ],
         [-0.06,  0.06,  0.02],
         [ 0.02,  0.02, -0.02],
         [ 0.01, -0.03,  0.02]],
        [[ 0.4 , -0.25,  0.  ],
         [ 0.24, -0.15,  0.  ],
         [ 0.05,  0.25, -0.25],
         [ 0.01,  0.05, -0.05],
         [ 0.05,  0.  ,  0.25],
         [ 0.01,  0.  ,  0.05],
         [-0.03,  0.12, -0.09],
         [-0.01,  0.04, -0.03],
         [-0.03,  0.03,  0.09],
         [-0.01,  0.01,  0.03],
         [ 0.  , -0.01,  0.02],
         [ 0.  , -0.01,  0.02],
         [-0.01,  0.04, -0.03],
         [ 0.  , -0.03,  0.06],
         [ 0.01,  0.  ,  0.05],
         [ 0.  ,  0.05, -0.1 ],
         [ 0.08, -0.05,  0.  ],
         [-0.05,  0.05,  0.15],
         [ 0.03,  0.15, -0.15],
         [ 0.05, -0.2 ,  0.15]]],
       [[[ 0.02, -0.01,  0.01],
         [ 0.04, -0.02,  0.02],
         [ 0.02,  0.  , -0.01],
         [ 0.02,  0.  , -0.01],
         [ 0.06,  0.01,  0.  ],
         [ 0.36,  0.06,  0.  ],
         [ 0.04,  0.02, -0.06],
         [ 0.02,  0.01, -0.03],
         [ 0.  ,  0.16, -0.12],
         [ 0.  ,  0.48, -0.36],
         [-0.06,  0.01,  0.06],
         [-0.36,  0.06,  0.36],
         [ 0.12,  0.06, -0.18],
         [-0.12,  0.02,  0.12],
         [ 0.12,  0.  , -0.06],
         [-0.06,  0.01,  0.06],
         [ 0.12, -0.06,  0.06],
         [ 0.  ,  0.08, -0.06],
         [ 0.04,  0.  , -0.02],
         [-0.02, -0.01,  0.03]],
        [[ 0.15, -0.25,  0.25],
         [ 0.09, -0.15,  0.15],
         [ 0.3 ,  0.  , -0.25],
         [ 0.06,  0.  , -0.05],
         [ 0.05,  0.25,  0.  ],
         [ 0.01,  0.05,  0.  ],
         [ 0.09,  0.03, -0.12],
         [ 0.03,  0.01, -0.04],
         [ 0.  ,  0.12, -0.03],
         [ 0.  ,  0.04, -0.01],
         [-0.01,  0.01,  0.01],
         [-0.01,  0.01,  0.01],
         [ 0.03,  0.01, -0.04],
         [-0.03,  0.03,  0.03],
         [ 0.06,  0.  , -0.05],
         [-0.05,  0.05,  0.05],
         [ 0.03, -0.05,  0.05],
         [ 0.  ,  0.2 , -0.05],
         [ 0.18,  0.  , -0.15],
         [-0.15, -0.05,  0.2 ]]],
       [[[-0.01,  0.  ,  0.03],
         [-0.02,  0.  ,  0.06],
         [ 0.01, -0.01,  0.01],
         [ 0.01, -0.01,  0.01],
         [ 0.  ,  0.01,  0.06],
         [ 0.  ,  0.06,  0.36],
         [ 0.06, -0.04, -0.02],
         [ 0.03, -0.02, -0.01],
         [ 0.12,  0.04, -0.12],
         [ 0.36,  0.12, -0.36],
         [-0.06,  0.07,  0.  ],
         [-0.36,  0.42,  0.  ],
         [ 0.18, -0.12, -0.06],
         [-0.12,  0.14,  0.  ],
         [ 0.06, -0.06,  0.06],
         [-0.06,  0.07,  0.  ],
         [-0.06,  0.  ,  0.18],
         [ 0.06,  0.02, -0.06],
         [ 0.02, -0.02,  0.02],
         [-0.03,  0.02,  0.01]],
        [[-0.25,  0.  ,  0.4 ],
         [-0.15,  0.  ,  0.24],
         [ 0.25, -0.25,  0.05],
         [ 0.05, -0.05,  0.01],
         [ 0.  ,  0.25,  0.05],
         [ 0.  ,  0.05,  0.01],
         [ 0.12, -0.09, -0.03],
         [ 0.04, -0.03, -0.01],
         [ 0.03,  0.09, -0.03],
         [ 0.01,  0.03, -0.01],
         [-0.01,  0.02,  0.  ],
         [-0.01,  0.02,  0.  ],
         [ 0.04, -0.03, -0.01],
         [-0.03,  0.06,  0.  ],
         [ 0.05, -0.05,  0.01],
         [-0.05,  0.1 ,  0.  ],
         [-0.05,  0.  ,  0.08],
         [ 0.05,  0.15, -0.05],
         [ 0.15, -0.15,  0.03],
         [-0.2 ,  0.15,  0.05]]],
       [[[-0.01,  0.01,  0.02],
         [-0.02,  0.02,  0.04],
         [ 0.  , -0.01,  0.02],
         [ 0.  , -0.01,  0.02],
         [ 0.01,  0.  ,  0.06],
         [ 0.06,  0.  ,  0.36],
         [ 0.02, -0.06,  0.04],
         [ 0.01, -0.03,  0.02],
         [ 0.16, -0.12,  0.  ],
         [ 0.48, -0.36,  0.  ],
         [ 0.01,  0.06, -0.06],
         [ 0.06,  0.36, -0.36],
         [ 0.06, -0.18,  0.12],
         [ 0.02,  0.12, -0.12],
         [ 0.  , -0.06,  0.12],
         [ 0.01,  0.06, -0.06],
         [-0.06,  0.06,  0.12],
         [ 0.08, -0.06,  0.  ],
         [ 0.  , -0.02,  0.04],
         [-0.01,  0.03, -0.02]],
        [[-0.25,  0.25,  0.15],
         [-0.15,  0.15,  0.09],
         [ 0.  , -0.25,  0.3 ],
         [ 0.  , -0.05,  0.06],
         [ 0.25,  0.  ,  0.05],
         [ 0.05,  0.  ,  0.01],
         [ 0.03, -0.12,  0.09],
         [ 0.01, -0.04,  0.03],
         [ 0.12, -0.03,  0.  ],
         [ 0.04, -0.01,  0.  ],
         [ 0.01,  0.01, -0.01],
         [ 0.01,  0.01, -0.01],
         [ 0.01, -0.04,  0.03],
         [ 0.03,  0.03, -0.03],
         [ 0.  , -0.05,  0.06],
         [ 0.05,  0.05, -0.05],
         [-0.05,  0.05,  0.03],
         [ 0.2 , -0.05,  0.  ],
         [ 0.  , -0.15,  0.18],
         [-0.05,  0.2 , -0.15]]],
       [[[ 0.  ,  0.03, -0.01],
         [ 0.  ,  0.06, -0.02],
         [-0.01,  0.01,  0.01],
         [-0.01,  0.01,  0.01],
         [ 0.01,  0.06,  0.  ],
         [ 0.06,  0.36,  0.  ],
         [-0.04, -0.02,  0.06],
         [-0.02, -0.01,  0.03],
         [ 0.04, -0.12,  0.12],
         [ 0.12, -0.36,  0.36],
         [ 0.07,  0.  , -0.06],
         [ 0.42,  0.  , -0.36],
         [-0.12, -0.06,  0.18],
         [ 0.14,  0.  , -0.12],
         [-0.06,  0.06,  0.06],
         [ 0.07,  0.  , -0.06],
         [ 0.  ,  0.18, -0.06],
         [ 0.02, -0.06,  0.06],
         [-0.02,  0.02,  0.02],
         [ 0.02,  0.01, -0.03]],
        [[ 0.  ,  0.4 , -0.25],
         [ 0.  ,  0.24, -0.15],
         [-0.25,  0.05,  0.25],
         [-0.05,  0.01,  0.05],
         [ 0.25,  0.05,  0.  ],
         [ 0.05,  0.01,  0.  ],
         [-0.09, -0.03,  0.12],
         [-0.03, -0.01,  0.04],
         [ 0.09, -0.03,  0.03],
         [ 0.03, -0.01,  0.01],
         [ 0.02,  0.  , -0.01],
         [ 0.02,  0.  , -0.01],
         [-0.03, -0.01,  0.04],
         [ 0.06,  0.  , -0.03],
         [-0.05,  0.01,  0.05],
         [ 0.1 ,  0.  , -0.05],
         [ 0.  ,  0.08, -0.05],
         [ 0.15, -0.05,  0.05],
         [-0.15,  0.03,  0.15],
         [ 0.15,  0.05, -0.2 ]]],
       [[[ 0.01,  0.02, -0.01],
         [ 0.02,  0.04, -0.02],
         [-0.01,  0.02,  0.  ],
         [-0.01,  0.02,  0.  ],
         [ 0.  ,  0.06,  0.01],
         [ 0.  ,  0.36,  0.06],
         [-0.06,  0.04,  0.02],
         [-0.03,  0.02,  0.01],
         [-0.12,  0.  ,  0.16],
         [-0.36,  0.  ,  0.48],
         [ 0.06, -0.06,  0.01],
         [ 0.36, -0.36,  0.06],
         [-0.18,  0.12,  0.06],
         [ 0.12, -0.12,  0.02],
         [-0.06,  0.12,  0.  ],
         [ 0.06, -0.06,  0.01],
         [ 0.  ,  0.12,  0.02],
         [ 0.06,  0.  , -0.08],
         [-0.02,  0.04,  0.  ],
         [ 0.03, -0.02, -0.01]],
        [[ 0.25,  0.15, -0.25],
         [ 0.15,  0.09, -0.15],
         [-0.25,  0.3 ,  0.  ],
         [-0.05,  0.06,  0.  ],
         [ 0.  ,  0.05,  0.25],
         [ 0.  ,  0.01,  0.05],
         [-0.12,  0.09,  0.03],
         [-0.04,  0.03,  0.01],
         [-0.03,  0.  ,  0.12],
         [-0.01,  0.  ,  0.04],
         [ 0.01, -0.01,  0.01],
         [ 0.01, -0.01,  0.01],
         [-0.04,  0.03,  0.01],
         [ 0.03, -0.03,  0.03],
         [-0.05,  0.06,  0.  ],
         [ 0.05, -0.05,  0.05],
         [ 0.  ,  0.03,  0.15],
         [ 0.05,  0.  , -0.2 ],
         [-0.15,  0.18,  0.  ],
         [ 0.2 , -0.15, -0.05]]]]),
    }
]