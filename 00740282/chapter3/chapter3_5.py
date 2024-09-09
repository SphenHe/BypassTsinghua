'''
编写函数 test_prime()，接受用户输入的某个自然数 n
调用例 3.12 实现的函数 is_prime() 输出其是否为素数的信息。要求使用异常处理机制。
'''

from chapter3_5_utils import is_prime

def test_prime(n: int) -> None:
    '''
    判断用户输入的自然数是否为素数

    参数:
        n: 用户输入的自然数

    返回:
        None
    '''
    try:
        if is_prime(n):
            print(f'{n} 是素数。')
        else:
            print(f'{n} 不是素数。')
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

def main():
    '''
    主函数

    通过调用 is_prime() 函数判断用户输入的自然数是否为素数。使用异常处理机制。
    '''
    n = int(input('请输入一个自然数：'))
    test_prime(n)

if __name__ == '__main__':
    main()
