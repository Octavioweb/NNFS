import numpy as np
import octoNumpy2 as np2


class Layer_Dense(object):
    def __init__(self,n_inputs,n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.weights = self.weights.tolist()
        self.biases = np.zeros((n_neurons))
        self.biases = self.biases.tolist()
        print(self.weights, '\n', self.biases)
        pass

    def forward(self,inputs):
        tensor = np2.dot(inputs, self.weights)
        self.output = np2.addBias(tensor, self.biases)

Layer_Dense(5,3)

import nnfs
from nnfs.datasets import spiral_data
nnfs.init()
import matplotlib.pyplot as plt

X,y = spiral_data(samples=100, classes=3)
dense1 = Layer_Dense(2,3)

dense1.forward(X.tolist())

print(dense1.output[:5])