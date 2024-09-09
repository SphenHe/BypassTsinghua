'''
挑战性问题。继续上一题。
现在考虑将多日多地的天气预报信息以逗号分隔值的形式保存在一个文本文件中。
其中，每个文本行保存单个城市某日的天气预报信息，其具体数据格式为“日期,城市,天气描述,最低温度,最高温度”。
注意，其中的逗号和数字均为半角字符（即与 ASCII 码兼容的字符），而文字描述可能为汉字，日期格式则为“YYYY-MM-DD”。
读入该文件，以元组型式保存每行天气预报信息，并将这些元组保存在一个列表对象中。
现在需要对这些数据排序。具体排序规则是：按照日期从小到大的次序排序，但对于具有同样日期的数据，各城市按照最高温度从大到小排序。
'''
from chapter5_1 import save_to_txt

FILE_PATH = 'weather_info.txt'

def read_weather_info(file_path):
    '''
    读取天气信息
    '''
    # 天气信息列表
    weather_list = []
    # 打开文件
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取每行天气信息
        for line in file:
            # 去除行尾换行符
            line = line.rstrip('\n')
            # 日期,城市,天气描述,最低温度,最高温度
            weather = tuple(line.split(','))
            # 添加到天气信息列表
            weather_list.append(weather)
    # 返回天气信息列表
    return weather_list

def sort_weather_info(weather_list):
    '''
    排序天气信息
    '''
    # 按照日期从小到大的次序排序，对于具有同样日期的数据，各城市按照最高温度从大到小排序
    weather_list.sort(key=lambda x: (x[0], -int(x[4])))
    # 返回排序后的天气信息
    return weather_list

def main():
    '''
    主函数
    '''
    # 从上一题的代码中保存天气信息到文件
    save_to_txt()
    # 读取天气信息
    weather_list = read_weather_info(FILE_PATH)
    # 排序天气信息
    weather_list = sort_weather_info(weather_list)
    # 输出排序后的天气信息
    for weather in weather_list:
        print(weather)

if __name__ == '__main__':
    main()
