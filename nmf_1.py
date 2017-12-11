#!/bin/python

from numpy import *
import plot_err
def load_data(file_path):
    f = open(file_path)
    V = []
    for line in f.readlines():
        lines = line.strip().split("\t")
        data = []
        for x in lines:
            data.append(float(x))
        V.append(data)
    return mat(V)
def train_off(V_Data,r,k,e):
    data_err = []
    err=[];
    H_data=[];
    length= len(V_Data)
    m,n=shape(V_Data[0])
    W = mat(random.random((m, r)))
    H = mat(random.random((n, r)))
    #模拟计算H矩阵
    for i in range(length):
        H_data.append(H)

    for count in range(length):
        err.append(W*H_data[count].T)
    # 计算误差矩阵



    # 开始迭代计算
    for x in range(k):
        err_sum = calculate_err(V_Data, err, length, m, n);
        print(err_sum)
        data_err.append(err_sum)
        if err_sum < e:
            break
        for i in range(length):
            a=V_data[i].T*W
            b=H_data[i]*W.T*W
            H_Q=H_data[i];
            for i_1 in range(n):
                for j_1 in range(r):
                    if b[i_1, j_1] != 0:
                        print("正在计算中....更新H_Q......行"+str(i_1)+" 列"+str(j_1))
                        H_Q[i_1, j_1] = H_Q[i_1, j_1] * a[i_1, j_1] / b[i_1, j_1]
            H_data[i]=H_Q;
        c=zeros([m,r])
        for i in range(length):
            c=c+(V_data[i]*H_data[i])
            print("执行中......c")
        d=zeros([m,r])
        for i in range(length):
            d=d+(W*H_data[i].T*H_data[i])
            print("执行中......d")
        for i_2 in range(m):
            for j_2 in range(r):
                if d[i_2, j_2] != 0:
                    print("正在计算中...更新W......行" + str(i_2) + " 列" + str(j_2))
                    W[i_2,j_2] = W[i_2,j_2] * c[i_2,j_2] / d[i_2, j_2]

        return W,H_data,data_err




def calculate_err(V_Data,err,length,m,n):
    err_sum = 0;
    for i in range(length):
        V = V_Data[i]
        E = err[i]
        err = V - E
        err_single = 0;
        # 计算每一个单个矩阵的误差和
        for i in range(m):
            for j in range(n):
                err_single += err[i, j] * err[i, j]
    # 计算每一个单个误差和
    err_sum = err_sum + err_single;
    return err_sum;
def train(V, r, k, e):
    data_err=[]
    m, n = shape(V)
    W = mat(random.random((m, r)))
    H = mat(random.random((r, n)))

    for x in range(k):
        #error
        V_pre = W * H
        E = V - V_pre
        #print E
        err = 0.0
        for i in range(m):
            for j in range(n):
                err += E[i,j] * E[i,j]
        print('误差:'+ str(err))
        data_err.append(err);
        if err < e:
            break

        a = W.T * V
        b = W.T * W * H
        #c = V * H.T
        #d = W * H * H.T
        for i_1 in range(r):
            for j_1 in range(n):
                if b[i_1,j_1] != 0:
                    H[i_1,j_1] = H[i_1,j_1] * a[i_1,j_1] / b[i_1,j_1]

        c = V * H.T
        d = W * H * H.T
        for i_2 in range(m):
            for j_2 in range(r):
                if d[i_2, j_2] != 0:
                    W[i_2,j_2] = W[i_2,j_2] * c[i_2,j_2] / d[i_2, j_2]

    return W,H,data_err


if __name__ == "__main__":
    file_path = "./result_nmf"

    V = load_data(file_path)
    #W, H,err = train(V, 2, 100, 1e-5)
    V_data=[V,V,V,V,V]
    W, H, data_err=train_off(V_data, 2, 100, 1e-5 )
    # print("=======打印V======")
    # print(V)
    # print("=======打印W======")
    # print(W)
    # print("=======打印H======")
    # print(H)
    # print("=======打印W * H======")
    # print( W * H)
    plot_err.plot_err_cure(data_err)

























# dim=size(X);                                    %计算x的规格
# X=double(X);
# B=10*rand(dim(1),r);                            %初始化BH，为非负数
# B=B./(ones(dim(1),1)*sum(B));                   %归一化B的每一列
#
# H=10*rand(r,dim(2));
# maxiter=100;                                    %最大迭代次数
# for iter=1:maxiter
#     H=H.*(B'*(X./(B*H)));
#     B=B.*((X./(B*H))*H');
#     B=B./(ones(dim(1),1)*sum(B));
# end