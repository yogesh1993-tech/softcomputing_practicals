"""
Practical 5: Write a program to implement Delta
Rule using Learning Rate

"""
import numpy as np
import matplotlib.pyplot as plt

epochs = np.arange(0, 50)
lr_decay = [0.001, 0.1, 0.5, 0.99]
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
plt_ind = np.arange(4) + 1


for decay, ind in zip(lr_decay, plt_ind): row, col = (ind - 1) // 2, (ind - 1) % 2
ax[row, col].plot(epochs, np.exp(-epochs * decay), c='cyan')
ax[row, col].set_title('Decay rate: ' + str(decay))
ax[row, col].set_xlabel('Epochs (t)')
ax[row, col].set_ylabel('Learning Rate (η^t)')
fig.tight_layout()
plt.show()




