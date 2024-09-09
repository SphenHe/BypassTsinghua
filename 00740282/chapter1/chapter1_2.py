'''
继续上一题。

现实生活中，储户在填定期存单时有“到期自动转存”选项，它表示在存单期满后自动转存为同样存期的新定期存单，结存的本金与利息总额将作为新本金。

计算自动转存一次和两次后的期满金额。
'''

import chapter1_1

def main():
    '''
    主函数

    说明：
    1. 接受用户输入的本金和利率
    2. 计算自动转存一次和两次后的期满金额
    '''
    principal = float(input('请输入本金：'))
    rate = float(input('请输入利率：'))

    # 一年期满后本金与利息总额
    money_0_year = chapter1_1.calculate_money_per_year(principal, rate)

    # 自动转存一次后的期满金额
    money_1_year = chapter1_1.calculate_money_per_year(money_0_year, rate)
    print('自动转存一次后的期满金额为：', money_1_year)

    # 自动转存两次后的期满金额
    money_2_year = chapter1_1.calculate_money_per_year(money_1_year, rate)
    print('自动转存两次后的期满金额为：', money_2_year)

if __name__ == '__main__':
    main()
