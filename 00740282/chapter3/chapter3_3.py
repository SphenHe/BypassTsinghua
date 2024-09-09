'''
编写函数 get_prime_gap()，接受整型参数 n，返回其后素数与前素数的差值。
例如，n 为 10 时，后素数为 11，前素数为 7，故此函数此时应返回 4。而当 n 为素数时，返回 0。
'''

def list_primes(n):
    '''
    返回小于等于 n 的所有素数
    '''
    primes = []

    if n < 2:
        return primes
    # 对2特殊处理
    primes.append(2)

    # 从3开始尝试分解
    divisor = 3  # 从3开始尝试分解
    while divisor <= n:
        # 检查当前divisor是否是质数
        is_prime = True
        for prime in primes:
            if divisor % prime == 0:
                is_prime = False
                break
        # 如果是质数，则进行分解
        if is_prime:
            primes.append(divisor)
        divisor += 2  # 尝试下一个数

    return primes

def get_prime_gap(n):
    '''
    返回整数 n 后素数与前素数的差值

    参数：
    - n：整数

    返回：
    - 差值
        - 如果 n 为素数，则返回 0
        - 如果 n 不为素数，则返回其后素数与前素数的差值
    '''
    # 列出所有小于等于 n 的素数
    primes = list_primes(n)

    # 判断 n 是否为素数
    if n in primes:
        return 0

    # 找到 n 前的素数
    prev_prime = primes[-1]

    # 找到 n 后的素数 / 找到下一个素数
    while primes[-1] < n:
        next_prime = primes[-1] + 2
        while True:
            is_prime = True
            for prime in primes:
                if next_prime % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(next_prime)
                break
            next_prime += 2

    return next_prime - prev_prime

def main():
    '''
    主函数

    说明：
    接收用户输入的整数，计算其后素数与前素数的差值，并打印输出
    '''
    n = int(input('请输入一个整数：'))
    gap = get_prime_gap(n)
    print(f'后素数与前素数的差值为：{gap}')

if __name__ == '__main__':
    main()
