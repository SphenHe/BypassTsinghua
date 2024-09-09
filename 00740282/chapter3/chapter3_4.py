'''
编写函数 get_int()，接受指定范围内的整数。
如果用户输入了非法数据，请求用户重新输入。要求使用异常处理机制。
'''

MIN_VALUE = 1
MAX_VALUE = 12

def get_int():
    '''
    获取指定范围 m 到 n 之间的内的整数

    返回：
    - 用户输入的整数
    '''
    while True:
        try:
            inp = int(input(f'请输入一个{MIN_VALUE}到{MAX_VALUE}之间的整数：'))
            if inp < MIN_VALUE or inp > MAX_VALUE:
                raise ValueError
            return inp
        except ValueError:
            print('输入错误，请重新输入')

def main():
    '''
    主函数

    说明：
    获取指定范围内的整数，如果用户输入了非法数据，则重新获取
    '''
    _n = get_int()

if __name__ == '__main__':
    main()
