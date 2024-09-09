'''
接受用户输入的两个数。

其中一个为一年期定期存款本金，一个为一年期定期存款利率。

计算一年期满后本金与利息总额。

说明：

（1）存款金额以人民币元为单位

（2）输入利率时不需要输入百分号，例如一年期定期存款年利率为 2.52%，输入 2.52 即可。
'''

def calculate_money_per_year(principal, rate):
    '''
    计算一年期满后本金与利息总额

    Args:
    principal: 本金
    rate: 利率

    Returns:
    一年期满后本金与利息总额
    '''
    return principal * (1 + rate / 100)

def main():
    '''
    主函数

    说明：
    1. 接受用户输入的本金和利率
    2. 计算一年期满后本金与利息总额
    3. 输出计算结果
    '''
    principal = float(input('请输入本金：'))
    rate = float(input('请输入利率：'))
    print('一年期满后本金与利息总额为：', calculate_money_per_year(principal, rate))

if __name__ == '__main__':
    main()
