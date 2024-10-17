import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

B0_MAGNETIC_FIELD = 6
N_DENSITY = 1
R_RADIUS = 6
A_RADIUS = 2
EPSILON_RATIO = 1/3
K_RATIO = 1.7
A_MASS = 2.5
ZEFF_ELECTRON = 1.5
Q_SAFETY_FACTOR = 1.7

KEV = 1E3 * 1.602E-19
MEV = 1E6 * 1.602E-19

tau_L = lambda T: 0.037 * EPSILON_RATIO**0.3 / Q_SAFETY_FACTOR**1.7 * A_RADIUS**1.17 * K_RATIO**1.7 * B0_MAGNETIC_FIELD**2.1 * A_MASS**1 / (N_DENSITY**-0.8 * T**1)
tau_H = lambda T: 0.28 * EPSILON_RATIO**0.3 / Q_SAFETY_FACTOR**3 * A_RADIUS**2.67 * K_RATIO**3.29 * B0_MAGNETIC_FIELD**3.48 * A_MASS**0.61 / (N_DENSITY**-0.91 * T**2.23)

S_B = lambda T: 5.355E-37*ZEFF_ELECTRON*(N_DENSITY*1e20)**2*T**0.5
S_k = lambda T,tau: 3*N_DENSITY*1E20*T*KEV/tau
S_alpha = lambda T: 1/20*(N_DENSITY*1e20)**2*ract.get("D-T",T)*17.6*MEV

T_data=np.logspace(0.1,2.5,num=200)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# 第一幅图
axs[0].plot(T_data, S_alpha(T_data), color='k', linewidth=3)
axs[0].plot(T_data, S_B(T_data))
axs[0].plot(T_data, S_k(T_data, tau_H(T_data)))
axs[0].plot(T_data, S_k(T_data, tau_L(T_data)))
axs[0].set_xscale("log")
axs[0].set_yscale("log")
axs[0].legend(["Alpha particle heating power", "Bremsstrahlung loss power", "H-mode thermal loss power", "L-mode thermal loss power"])
axs[0].set_title("Power Balance Separately")

# 第二幅图
S_ttlH = S_B(T_data) + S_k(T_data, tau_H(T_data))
theidx = np.where(np.diff(S_ttlH > S_alpha(T_data)))[0]    # S_ttlH与S_alpha两条线的交点

axs[1].plot(T_data, S_alpha(T_data), color='k', linewidth=3)
axs[1].plot(T_data, S_ttlH)
axs[1].plot(T_data, S_B(T_data) + S_k(T_data, tau_L(T_data)))
axs[1].text(T_data[theidx[0]], S_ttlH[theidx[0]] / 1.5, "Ignition", va="top", size="large")
axs[1].text(T_data[theidx[1]], S_ttlH[theidx[1]] / 1.5, "Stable", va="top", size="large")
axs[1].scatter(T_data[theidx], S_ttlH[theidx])  # 功率平衡点及其tag
axs[1].legend(["Alpha particle heating power", "Bremsstrahlung + H-mode total loss power", "Bremsstrahlung + L-mode total loss power", "Power balance point"])
axs[1].set_xscale("log")
axs[1].set_yscale("log")
axs[1].set_title("Power Balance Summarily")

plt.tight_layout()
plt.savefig("./../img/1.pdf")
# plt.show()
