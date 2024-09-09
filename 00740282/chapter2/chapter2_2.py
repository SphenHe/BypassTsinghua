'''
与习题 2.2 有关。

接受用户输入的年月日信息，输出该日为该年的第几天。

计算和输出时，1 月 1 日记为第 1 天，1 月 2 日记为第 2 天，以此类推。

注：需要考虑闰年问题；不得使用 Python 标准库中的函数或类。
'''

import chapter2_1

def calc_days(year, month, day):
    '''
    计算该日为该年的第几天

    Args:
    year: 年份
    month: 月份
    day: 日

    Returns:
    该日为该年的第几天
    '''
    while month > 1:
        day += chapter2_1.month_days_branch(year, month - 1)
        month -= 1
    return day

def main():
    '''
    主函数

    说明：
    1. 接受用户输入的年月日信息
    2. 输出该日为该年的第几天
    '''
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))
    day = int(input('请输入日：'))
    if year < 0 or month < 1 or month > 12 or day < 1 or \
            day > chapter2_1.month_days_branch(year, month):
        print('输入信息有误')
    else:
        print(f'{year} 年 {month} 月 {day} 日是该年的第 {calc_days(year, month, day)} 天')

if __name__ == '__main__':
    main()
