'''
编写函数，统计一个字符串中所有元音字母的出现总次数及出现总频率。函数应同时返回这两者。
'''

def calculate_vowels(string):
    '''
    统计字符串中所有元音字母的出现总次数及出现总频率
    '''
    # 元音字母
    vowels = 'aeiouAEIOU'
    # 计数器
    count = 0
    # 遍历字符串
    for char in string:
        # 判断字符是否为元音字母
        if char in vowels:
            count += 1
    # 返回元音字母出现总次数及出现总频率
    return count, count / len(string)

def main():
    '''
    主函数

    说明：
    接收用户输入的字符串，统计字符串中所有元音字母的出现总次数及出现总频率，并打印输出
    '''
    string = input('请输入一个字符串：')
    count, frequency = calculate_vowels(string)
    print(f'字符串中所有元音字母的出现总次数为：{count}')
    print(f'字符串中所有元音字母的出现总频率为：{frequency:.2f}')

if __name__ == '__main__':
    main()
