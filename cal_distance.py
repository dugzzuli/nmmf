#########################################
# 计算时间序列之间的距离
#
#########################################

from numpy import *
import numpy as np
import operator
from dtw import dtw

# create a dataset which contains 4 samples with 2 classes
def createDataSet():
    # create a matrix: each row as a sample
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A', 'A', 'B', 'B']  # four samples and two classes
    return group, labels

def my_custom_norm(x, y):
    return (x * x) + (y * y)
def calDistance(A,B):
    dist, cost, acc, path = dtw(A, B, dist=my_custom_norm)
    return dist

def eNN(dataSet,e):
    numSamples = dataSet.shape[0]  # shape[0] stands for the num of row
    mat=zeros([numSamples,numSamples])
    for i in range(numSamples):
        for j in range(numSamples):
            if (i!=j):
                mat[i,j]=calDistance(np.array(dataSet[i,:]).reshape(-1, 1),np.array(dataSet[j,:].reshape(-1, 1)));
    for i in range(numSamples):
        for j in range(numSamples):
            if(mat[i,j]<e):
                mat[i, j]=0;
    return mat
if __name__ == '__main__':
    std_data=mat([[1,2,3,4,5,5,6,7,8,9,89],[1,2,3,4,5,5,6,7,8,9,89],[1,2,3,4,5,5,6,7,8,9,89]])
    print(std_data)
    mat=eNN(std_data,15)
    print(mat)