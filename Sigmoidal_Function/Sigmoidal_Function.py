"""
Practical 2: Calculate the output of Neural net
using Sigmoidal Function

"""
import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))

x=1
print(f"Applying Sigmod Activation on {x} gives {round(sig(x),2)}")
x = -10
print(f"Applying Sigmoid Activation on {x} gives {round(sig(x), 2)}")
x = 0
print(f"Applying Sigmoid Activation on {x} gives {round(sig(x), 2)}")
x = 15
print(f"Applying Sigmoid Activation on {x} gives {round(sig(x), 2)}")
x = -2
print(f"Applying Sigmoid Activation on {x} gives {round(sig(x), 2)}")
