'''
编写函数。接受用户输入的字符串，判断其是否为合法 Python 标识符。
'''

from keyword import iskeyword

def is_valid_identifier(s):
    '''
    判断字符串是否为合法 Python 标识符

    参数：
    - s：字符串

    返回：
    - 若 s 为合法 Python 标识符，返回 True；
    - 否则，返回 False。
    '''
    if iskeyword(s):
        return False
    if not s.isidentifier():
        return False
    return True

def main():
    '''
    主函数

    通过调用 is_valid_identifier() 函数判断用户输入的字符串是否为合法 Python 标识符。
    '''
    s = input('请输入字符串：')
    if is_valid_identifier(s):
        print('合法标识符')
    else:
        print('非法标识符')

if __name__ == '__main__':
    main()
