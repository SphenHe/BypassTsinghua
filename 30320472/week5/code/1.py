import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# 定义读取数据和处理数据的类

class GETDATA:
    def __init__(self,filename):    # 初始化，从给定的文件中载入数据
        ## 初始化了两个变量：
        ## data：一个dataframe，储存读取的原始数据
        ## types：一个list，储存了这么一些反应的数据
        self.data = pd.read_csv(filename,comment="#") #用pandas库读取数据
        column_names=list(self.data.columns.values)
        self.types = column_names[1:]

    def get(self,type,v_in):    # 一个查询数据的简单方法
        ## 输入两个参数(type,v_in)
        ## type：该反应的type，应包含在types中
        ## v_in：输入值，能量或者温度，可以是一个数、list、array等
        ## 返回 -> 对应的线性插值得到的截面或反应率数据
        v_inl=np.log10(v_in)
        x_values=self.data.iloc[:,0]
        assert (type in self.types), "查无此反应！"
        assert ((v_inl > min(x_values)).all() and (v_inl < max(x_values)).all()), "有输入值超量程！"
        v_out=10**np.interp(v_inl,x_values,self.data[type]) # 线性插值
        return v_out

# 读取反应截面和反应率的数据
xsec=GETDATA("data_of_crosssec.txt")
ract=GETDATA("data_of_reactiv.txt")
## =============================================================================

etas = [0, 0.3, 0.5]

# Read the data
T_log = np.logspace(0.5,3,num=100)     # 自定义一串能量，logspace()就是10**linespace()
ract_log = ract.get("D-T", T_log)

T = 10**T_log
ract = 10**ract_log

# Calculate the cross section and n_B\tau_E
for eta in etas:
    y = 3*T*(1-eta)/((1+4*eta)/20*ract*17.6E3-(1-eta)*5.355E-37*np.sqrt(T))/(1.602E-19)

    y_log = np.log10(y)

    plt.plot(T_log, y_log)  # get()数据，并画图。注意如果不show()的话就相当于hold on
    plt.legend(etas)

plt.title("ignition conditions")
plt.xlabel(r"$T$ [keV]")
plt.ylabel(r"$n_B\tau_E$ [m$^{-3}$s]")
plt.xscale('log')
plt.yscale('log')
# plt.axis(10.**np.array([0, 3, 20, 40]))
plt.grid(True)
plt.savefig("./../img/1.pdf") # 保存图片
plt.show() # 把上面画的图show()出来
