'''
接受用户输入的 [1, 12] 范围内的整数，对其输入进行数据有效性检查。
即，当用户输入了范围外的整数时，提醒用户输入有误。
分别使用匹配语句、异常处理机制和断言语句实现之。
'''

def check_with_match(num):
    '''
    使用匹配语句检查用户输入的整数是否在 [1, 12] 范围内
    '''
    match num:
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
            print('使用匹配语句检查，输入有效！')
        case _:
            print('使用匹配语句检查，输入无效！')

def check_with_exception(num):
    '''
    使用异常处理机制检查用户输入的整数是否在 [1, 12] 范围内
    '''
    try:
        if num < 1 or num > 12:
            raise ValueError
    except ValueError:
        print('使用异常处理机制检查，输入无效！')
    else:
        print('使用异常处理机制检查，输入有效！')

def check_with_assert(num):
    '''
    使用断言语句检查用户输入的整数是否在 [1, 12] 范围内
    '''
    assert 1 <= num <= 12, '使用断言语句检查，输入无效！'
    print('使用断言语句检查，输入有效！')

def main():
    '''
    主函数

    说明：
    使用匹配语句、异常处理机制和断言语句分别检查用户输入的整数是否在 [1, 12] 范围内
    '''

    num = int(input('请输入一个1-12之间的整数：'))
    check_with_match(num)
    check_with_exception(num)
    check_with_assert(num)

if __name__ == '__main__':
    main()
