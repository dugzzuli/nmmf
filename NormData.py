import numpy as np
from sklearn import *

def minMaxMean(A):
    minmaxTransformer =preprocessing.MinMaxScaler(feature_range=(0, 1))
    train_transformer = minmaxTransformer.fit_transform(A)
    return train_transformer
def Mean(A):
    mean_A=np.mean(A)
    mean_data=np.tile(mean_A,len(A))
    E=A-mean_data
    max_A=np.max(A)
    min_A=np.min(A)
    standard_data=(E/(max_A-min_A))
    return  standard_data
def standard_data(Data):
    m,n=np.shape(Data)
    data_re=[];
    for i in range(m):
        std=Mean(Data[i])
        data_re.append(std)
    return np.mat(data_re)
if __name__ == '__main__':
    std_data=standard_data([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
    print(standard_data)
    for i in range(3):
        print(std_data[i])