#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:52:36 2020

@author: jameselijah

Tensorflow BAsics Tutorial (Linear Regression) - 
Source: https://www.youtube.com/watch?v=Xiab2JhwzYY
Credits to Mark Jay

"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() #to mediate AttributeError: module 'tensorflow' has no attribute 'placeholder'

import numpy as np
import os
import sys
import traceback
import pandas as pd
import matplotlib.pyplot as plt

learning_rate = 0.01
epochs = 200

n_samples = 30
train_x = np.linspace (0,20,n_samples)
train_y = 3 * train_x + np.random.randn(n_samples)

plt.plot (train_x, train_y, 'o')
plt.plot(train_x, 3 * train_x)
plt.show()

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#Defining the variables 

W = tf.Variable(np.random.randn(),name = "weights") #weight is simply just the gradient of graph
B = tf.Variable(np.random.randn(), name = "bias") #this is simply just the y-axis intercept

prediction = tf.add(tf.multiply(X, W), B) #Y = mX + C --> Basically the graph

# Cost function = Need this to make tensor flow try to minimize and its going to be playing with wieghts and bias, 
# in order to find the lowest value that it can

cost_function = tf.reduce_sum ((prediction - Y)**2/ (2 * n_samples))