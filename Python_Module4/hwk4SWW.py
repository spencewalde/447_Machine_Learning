# -*- coding: utf-8 -*-
"""homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sq8sNa56gCUuteijp4YaKztwuQ0jWecr
"""

import numpy as np
import pandas as pd

def confu_matrix(target, output):
    K = len(np.unique(target))
    result = np.zeros((K,K))

    for i in range(len(target)):
        result[target[i]-1][output[i]-1] += 1

    return result

def confu_acc(target,output):
      return (target == output).sum() / float(len(target))

dataset = pd.read_csv('HW_TestingMetrics.csv', skiprows=[0,3,6,9,12,15,18,21,24,27,30],header=None)
print(dataset)
dataset = dataset.iloc[:,1:].values
acc = []
for i in range(0, len(dataset),2):
    print('test')
  
    print(confu_matrix(dataset[i],dataset[i+1]))

    acc.append(confu_acc(dataset[i],dataset[i+1]))
print('Accuracy:')
print(acc)