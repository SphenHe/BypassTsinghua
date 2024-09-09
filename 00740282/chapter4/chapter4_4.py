'''
编写程序，随机生成 10 个 [0.0, 1.0] 之间的实数
使用 pickle 模块将它们持久化至文件“floats_dump_file.dat”中。随后从该文件中读取这些浮点数并输出。
注：不得使用元组、列表等复合数据对象存储这些实数。
'''

import pickle
import random

FLOAT_NUM = 10

def save_floats():
    '''
    保存浮点数
    '''
    with open('floats_dump_file.dat', 'wb') as f:
        for _ in range(FLOAT_NUM):
            # 生成随机浮点数并写入文件
            pickle.dump(random.random(), f)

def load_floats():
    '''
    读取浮点数
    '''
    with open('floats_dump_file.dat', 'rb') as f:
        for _ in range(FLOAT_NUM):
            # 读取文件中的浮点数并输出
            print(pickle.load(f))

def main():
    '''
    主函数
    '''
    save_floats()
    load_floats()

if __name__ == '__main__':
    main()
