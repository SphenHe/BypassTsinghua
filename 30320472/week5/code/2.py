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
# 
p={ "pure":[3.6,0.67],
    "scat":[10.0,0.34],
    "fcat":[14.4,0.62],}

# T in keV, E in MeV, k in 1
ignitcon0 = lambda T,E,k : 3*T*1e3*1.6e-19/(k*0.5*ract.get("D-D(total)",T)*E*1e6*1.6e-19 - 5.355e-37*1*T**0.5)
ignitcon = lambda T,type : ignitcon0(T,p[type][0],p[type][1])

# print(ignitcon(100,"pure"))
T_data=np.logspace(1,3,num=100)
ignitmin=dict()
for type in ["pure","scat","fcat"]:
    ignit_data=ignitcon(T_data,type)
    ignit_data[ignit_data<0]=np.inf
    plt.plot(T_data,ignit_data)

    T_min = T_data[ignit_data==np.min(ignit_data)]
    ignitmin[type]=ignitcon(T_min,type)
    plt.scatter(T_min,ignitmin[type])

plt.xscale('log')
plt.yscale('log')
plt.xlabel("$T$ [keV]")
plt.ylabel("$n \\tau _E$ [SI(m$^3$/s)]")
plt.legend(["pure","pure-min: %.2e"%ignitmin["pure"][0],
            "scat","scat-min: %.2e"%ignitmin["scat"][0],
                        "fcat","fcat-min: %.2e"%ignitmin["fcat"][0],])
plt.title("Ignition conditions")
plt.grid()
plt.savefig("./../img/2.pdf")
# plt.show()
