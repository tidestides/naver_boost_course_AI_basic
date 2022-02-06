import numpy as np

xy = np.array([[1.,2.,3.,4.,5.,6.],
            [10.,20.,30.,40.,50.,60.]])
x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.uniform(0,1,1)
bias = np.random.uniform(0,1,1)

print(beta_gd,bias)
