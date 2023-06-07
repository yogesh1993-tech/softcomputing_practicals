import np as np
import numpy as np
w = np.array([1,-1,0,0.5]).transpose()

Xi = [
np.array([1, -2, 1.5, 0]).transpose(),
np.array([1, -0.5, -2, -1.5]).transpose(),
np.array([0, 1, -1, 1.5]).transpose(),
]

c = 1 #Learning constant

for i in range (len(Xi)):
    net=sum(w.transpose()*Xi[i])
    Fnet=np.sign(net)
    dw= c * Fnet * Xi[i]
    W = w + dw



print(f"Final weight matrix : {W}")
print(f"Iterations : {i+1}")


