'''
将形如 y = f(x) 这样的数学函数以键值对的形式保存在字典中。
其中，键为函数名称对应的字符串，值为函数对象。此后使用函数名称匹配对应的函数对象，调用该函数。
以常用三角函数为例实现本题。如cos x, sin x, tan x等。
'''

import math

functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan
}

def call_func(operators, x):
    '''
    根据函数名称调用对应的函数
    '''
    return functions[operators](x)

def main():
    '''
    主函数
    '''
    func = input('请输入函数名称(sin, cos, tan):')
    x = float(input('请输入x的值:'))
    print(call_func(func, x))

if __name__ == '__main__':
    main()
