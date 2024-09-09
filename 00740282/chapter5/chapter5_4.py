'''
挑战性问题。继续上一题。快算 24 游戏（单次游戏）。
编写程序，随机生成 4 个 [1, 13] 之间的整数，数字允许重复，判断其能否算出 24。如果能，给出其计算公式。
本游戏的一般计算规则为：（1）仅允许进行四则算术运算，即仅能进行加减乘除运算，但中间计算结果可以为分数；（2）允许使用括号改变操作符的优先级。
'''

import random
from itertools import permutations
from chapter5_3 import evaluate_expression

def generate_expressions(numbers):
    """
    递归生成所有可能的表达式，并去除无用的括号

    参数:
        numbers (list): 包含数字的列表

    返回:
        generator: 生成所有可能的表达式
    """
    if len(numbers) == 1:
        yield str(numbers[0])
    else:
        for i in range(1, len(numbers)):
            for left in generate_expressions(numbers[:i]):
                for right in generate_expressions(numbers[i:]):
                    for op in ['+', '-', '*', '/']:
                        # 判断是否需要括号
                        if op in ['*', '/']:
                            # 乘号和除号需要考虑括号的添加
                            if ('+' in left or '-' in left) and ('+' in right or '-' in right):
                                yield f"({left}){op}({right})"
                            elif '+' in left or '-' in left:
                                yield f"({left}){op}{right}"
                            elif '+' in right or '-' in right:
                                yield f"{left}{op}({right})"
                            else:
                                yield f"{left}{op}{right}"
                        elif op in ['+', '-']:
                            # 加号和减号不需要考虑括号的添加
                            yield f"{left}{op}{right}"

def can_calculate_24(numbers):
    """
    判断是否能通过四则运算得到 24

    参数:
        numbers (list): 包含数字的列表

    返回:
        list: 包含所有能通过四则运算得到 24 的表达式
    """

    available_expression = set()
    for perm in permutations(numbers):
        for expression in generate_expressions(list(perm)):
            try:
                if abs(evaluate_expression(expression) - 24) < 1e-6:
                    available_expression.add(expression)
            except ZeroDivisionError:
                continue
    return list(available_expression)

def main():
    '''
    主函数
    '''
    numbers = [random.randint(1, 13) for _ in range(4)]
    print(f'生成的四个数字为：{numbers}')
    available_expression = can_calculate_24(numbers)
    if available_expression:
        print(f'可以通过四则运算得到 24，共有 {len(available_expression)} 种表达式：')
        for expression in available_expression:
            print(f'第 {available_expression.index(expression) + 1} 种表达式：{expression}')
    else:
        print('不能通过四则运算得到 24')

if __name__ == '__main__':
    main()
