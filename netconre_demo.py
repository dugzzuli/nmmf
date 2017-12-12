from numpy import *
import numpy as np
import operator
from dtw import dtw
import cal_distance as cal
import NormData
import  nmf_1
if __name__ == "__main__":
    file_path = "./result_nmf"

    V = nmf_1.load_data(file_path)
    #W, H,err = train(V, 2, 100, 1e-5)
    V_data=[V,V,V,V,V]
    V_data_norm=[];
    for i in range(len(V_data)):
        V_data_norm.append(NormData.standard_data(V_data[i]))
    W, H, data_err=nmf_1.train_off(V_data_norm, 2, 10000, 1e-5 )
