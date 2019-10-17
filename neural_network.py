# -*- coding: utf-8 -*-
"""Neural_Network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d3Z6uIVnIo1l7w-BR-Eq510XxObsZNvs
"""

import numpy as np


np.random.seed(0)
X = np.array([[1.0, 0.7]])
y_true = np.array([1.80])


def initialize_param(n_x, n_h, n_y):
  W1 = np.random.randn(n_h, n_x)
  W2 = np.random.randn(n_h, n_y)
  return W1, W2

def forward_propagation(X, W1, W2):
  H = np.dot(X, W1)
  y_pred = np.dot(H, W2)
  return H, y_pred

def calc_error(y_true, y_pred):
  return y_pred - y_true

def back_propagation(X, W1, W2, learning_rate = 0.01, iters = 1000, precision = 0.000001):
  
  H, y_pred = forward_propagation(X, W1, W2)
  
  for i in range(iters):
    error = calc_error(y_true, y_pred)
    W2 = W2 - learning_rate * error * H.T
    W1 = W1 - learning_rate * error * X.T * W2.T
    
    _, y_pred = forward_propagation(X, W1, W2)
    
    print('Iter {}, y_pred {}, error {}' .format(i, y_pred[0][0], calc_error(y_true, y_pred)[0][0]))
  
    if abs(error) < precision:
      break
      
  return W1, W2
  
def predict(X, W1, W2):
  _, y_pred = forward_propagation(X, W1, W2)
  return y_pred

def build_model():
  #initializacja
  W1, W2 = initialize_param(2,2,1)
  #propagacja wstecz
  W1, W2 = back_propagation(X, W1, W2)
  
  model = {'W1': W1, 'W2' : W2}
  return model

build_model()

