'''
编写函数，计算圆周率。
存在圆心在直角坐标系原点且半径为 1 的圆及其外切正方形。
为计算方便，仅考虑它们位于第一象限的那四分之一部分。
随机生成该四分之一正方形中的一系列点，散布于四分之一圆内比例即为圆周率四分之一。
'''

import numpy as np

SIM_NUMBER = 10000000

def montocarlo_pi(n):
    '''
    计算圆周率

    参数：
    n -- 随机点的数量

    返回：
    圆周率的近似值
    '''
    count = 0
    x = np.random.random(n)
    y = np.random.random(n)
    count = np.sum(x**2 + y**2 <= 1)
    return count / n * 4

def main():
    '''
    主函数

    说明：
    通过调用 montocarlo_pi() 函数计算圆周率。
    '''
    print('圆周率的近似值为：', montocarlo_pi(SIM_NUMBER))

if __name__ == '__main__':
    main()
