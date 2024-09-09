'''
接受用户输入的年份和月份，返回该月的天数。要求分别使用分支结构与匹配语句实现。
'''

def is_leap_year(year):
    '''
    判断是否为闰年

    Args:
    year: 年份

    Returns:
    是否为闰年
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def month_days_branch(year, month):
    '''
    返回该月的天数，使用分支结构实现

    Args:
    year: 年份
    month: 月份

    Returns:
    该月的天数
    '''
    if year < 0 or month < 1 or month > 12:
        return None
    elif month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return None

def month_days_case(year, month):
    '''
    返回该月的天数，使用匹配语句实现

    Args:
    year: 年份
    month: 月份

    Returns:
    该月的天数
    '''
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            match is_leap_year(year):
                case True:
                    return 29
                case False:
                    return 28
        case _:
            return None

def main():
    '''
    主函数

    说明：
    1. 接受用户输入的年份和月份
    2. 返回该月的天数
    '''
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))

    days = month_days_branch(year, month)
    if days:
        print(f'在使用分支结构计算时，{year}年{month}月有{days}天')
        print(f'在使用匹配语句计算时，{year}年{month}月有{days}天')
    else:
        print('输入的月份有误！')

if __name__ == '__main__':
    main()
