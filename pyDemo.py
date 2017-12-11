from numpy import *
import numpy as np
import nimfa as nm
import nmf
import plot_err
m=5
n=5
W = mat(random.random((m, n)))
V=np.array([W,W,W])
w2 =mat(random.random((5, 2)))
h2 =mat(random.random((5, 2)))


(wo, ho) = nmf.nmf(V[:,:,0], w2, h2, 0.001, 10, 10)
print((wo, ho))


