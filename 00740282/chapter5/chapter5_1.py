'''
假设天气预报的格式为形如“(日期, 城市, 天气描述, 最低温度, 最高温度)”的五元组。

编写程序，以嵌套元组的形式保存下述城市天气预报，并按照最高温度从大到小的次序进行排序。

其中日期 day 使用 datetime 模块中的 date 类构造。实现本题时，可以将下述天气信息替换为当日播报的内容。

t1 = (day, "北京", "多云", 20, 34)

t2 = (day, "哈尔滨", "小雨", 10, 15)

t3 = (day, "上海", "多云转小雨", 19, 25)

t4 = (day, "武汉", "中雨", 19, 24)

t5 = (day, "深圳", "阴转阵雨", 25, 30)

t6 = (day, "西安", "小雨转多云", 16, 30)

t7 = (day, "成都", "阴转晴", 17, 29)

t8 = (day, "香港", "阵雨", 25, 28)
'''

import datetime

SAVE_PATH = 'weather_info.txt'

def read_weather_info():
    '''
    读取天气预报信息
    '''
    # 日期
    day = datetime.date.isoformat(datetime.date.today())
    # 天气预报
    t1 = (day, "北京", "多云", 20, 34)
    t2 = (day, "哈尔滨", "小雨", 10, 15)
    t3 = (day, "上海", "多云转小雨", 19, 25)
    t4 = (day, "武汉", "中雨", 19, 24)
    t5 = (day, "深圳", "阴转阵雨", 25, 30)
    t6 = (day, "西安", "小雨转多云", 16, 30)
    t7 = (day, "成都", "阴转晴", 17, 29)
    t8 = (day, "香港", "阵雨", 25, 28)
    # 天气预报列表
    weather_list = [t1, t2, t3, t4, t5, t6, t7, t8]
    return weather_list

def save_to_txt():
    '''
    保存天气预报信息到 CSV 文件
    '''
    # 打开文件
    weather_list = read_weather_info()
    with open(SAVE_PATH, 'w', encoding='utf-8') as file:
        # 保存每行天气预报信息
        for weather in weather_list:
            # 日期,城市,天气描述,最低温度,最高温度
            line = ','.join(map(str, weather))
            # 写入文件
            file.write(line + '\n')

def main():
    '''
    主函数
    '''
    weather_list = read_weather_info()
    # 按照最高温度从大到小的次序进行排序
    weather_list.sort(key=lambda x: x[4], reverse=True)
    # 输出排序后的天气预报
    for weather in weather_list:
        print(weather)

if __name__ == '__main__':
    main()
