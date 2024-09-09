'''
设计算法，将某个合数 n 分解为若干素因子的乘积。例如，6 = 2 * 3。
'''

def decompose(num):
    '''
    将合数分解为若干素因子的乘积

    分解原理，将合数 num 从 2 开始，依次除以各个质数，直到 num 为 1 为止

    在除以质数的时候，需要生成一个质数筛来判断质数，已经判断好的质数可以存储在一个列表中，来加快判断速度

    参数：
    - num：合数

    返回：
    - factors：素因子列表
    '''
    if not isinstance(num, int) or num < 2:
        raise ValueError("输入必须是非负整数且大于1")

    factors = []
    prime_memory = [2]  # 用于存储已知的质数

    # 对2特殊处理
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    # 从3开始尝试分解
    divisor = 3  # 从3开始尝试分解
    while num > 1:
        # 检查当前divisor是否是质数
        is_prime = True
        for prime in prime_memory:
            if divisor % prime == 0:
                is_prime = False
                break
        # 如果是质数，则进行分解
        if is_prime:
            while num % divisor == 0:
                factors.append(divisor)
                num //= divisor
            prime_memory.append(divisor)
        divisor += 2  # 尝试下一个数

    return factors

def main():
    '''
    主函数

    说明：
    接收用户输入的合数，将其分解为若干素因子的乘积，并打印输出
    '''
    num = int(input('请输入一个合数：'))
    # 分解合数
    factors = decompose(num)
    # 打印输出
    print(f'{num} = ', end='')
    for i, factor in enumerate(factors):
        print(factor, end='')
        if i < len(factors) - 1:
            print(' * ', end='')

if __name__ == '__main__':
    main()
