'''
挑战性问题。
接受用户输入的四则运算表达式，使用栈进行表达式求值。
算术表达式是形如“1 - (2 + 3) * 4”这样的表达式。

参考资料：[中缀表达式转后缀表达式](https://zq99299.github.io/dsalg-tutorial/dsalg-java-hsp/05/05.html)

'''

def precedence(op):
    """返回操作符的优先级"""
    match op:
        case '+': return 1
        case '-': return 1
        case '*': return 2
        case '/': return 2
        case _: return 0

def apply_operator(a, b, op):
    """应用操作符进行计算"""
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b

def infix_to_postfix(expression):
    """
    将中缀表达式转换为后缀表达式

    参数:
        expression (str): 中缀表达式

    返回:
        list: 后缀表达式的列表形式

    """

    output = []
    operators = []
    i = 0
    while i < len(expression):
        # 跳过空格
        if expression[i].isspace():
            i += 1
            continue
        # 处理负数和正数
        if expression[i].isdigit() or (
            expression[i] == '-' and (i == 0 or expression[i-1] in '(*+-/')
        ):
            num = expression[i]
            i += 1
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            i -= 1
            output.append(float(num))
        # 处理左括号
        elif expression[i] == '(':
            operators.append(expression[i])
        # 处理右括号
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()
        # 处理操作符
        elif expression[i] in '+-*/':
            while operators and precedence(operators[-1]) >= precedence(expression[i]):
                output.append(operators.pop())
            operators.append(expression[i])
        i += 1
    while operators:
        output.append(operators.pop())
    return output

def evaluate_postfix(postfix):
    """计算后缀表达式的值

    参数:
        postfix (list): 后缀表达式，包含数字和运算符

    返回:
        float: 后缀表达式的计算结果

    异常:
        IndexError: 如果后缀表达式不合法或无法计算

    """
    stack = []
    for token in postfix:
        if isinstance(token, (int, float)):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            result = apply_operator(a, b, token)
            stack.append(result)
    return stack[0]

def evaluate_expression(expression):
    """接受用户输入的四则运算表达式并求值"""
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    return result

def main():
    '''
    主函数
    '''
    # 用户输入表达式
    expression = input('请输入四则运算表达式：')
    # 计算结果
    result = evaluate_expression(expression)
    # 输出结果
    print('计算结果：', result)

if __name__ == '__main__':
    main()
