'''
接受用户输入的两个整数，求其阶乘之和并输出结果。
'''

def factorial(n):
    '''
    求n的阶乘

    参数：
    n -- 整数

    返回：
    n的阶乘
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    '''
    主函数

    说明：
    1. 接受用户输入的两个整数
    2. 求其阶乘之和并输出结果
    '''
    num1 = int(input('请输入第一个整数：'))
    num2 = int(input('请输入第二个整数：'))

    sum_of_factorial = factorial(num1) + factorial(num2)
    print('阶乘之和为：', sum_of_factorial)

if __name__ == '__main__':
    main()
