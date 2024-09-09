'''
打印所有 100 至 999 之间的水仙花数。所谓水仙花数，是指各位数字的立方和为该数字本身的整数。
'''

def is_narcissistic_number(num):
    '''
    判断一个数是否为水仙花数，是则返回 True，否则返回 False
    '''
    # 个位数
    a = num % 10
    # 十位数
    b = num // 10 % 10
    # 百位数
    c = num // 100
    # 判断是否为水仙花数
    return num == a ** 3 + b ** 3 + c ** 3

def main():
    '''
    主函数

    说明：
    打印所有 100 至 999 之间的水仙花数
    '''
    for i in range(100, 1000):
        if is_narcissistic_number(i):
            print(i)

if __name__ == '__main__':
    main()
