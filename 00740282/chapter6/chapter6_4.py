'''
使用面向对象架构重新实现第 5.16 题。

【5.16】快算 24 游戏（回合制）。
编写程序，以每次计算为一局，以 10 局为一轮。
对于每次生成的 4 个整数，接受用户输入的表达式，判断其是否计算正确。一轮结束时，统计用户该轮的胜率。
'''

import random
import re
from chapter5_3_utils import evaluate_expression
from chapter5_4_utils import can_calculate_24

class Game24:
    '''
    24点游戏 类

    Attributes:
        win_count (int): 用户胜利的局数

    Methods:
        generate_question: 生成一个可以计算出24的四个数字
        is_valid_expression: 判断表达式是否合法
        play_round: 进行一轮游戏
        main: 主函数
    '''
    def __init__(self):
        self.win_count = 0

    def generate_question(self):
        '''
        生成一个可以计算出24的四个数字

        返回:
            list: 包含四个数字的列表
        '''
        numbers = [random.randint(1, 13) for _ in range(4)]
        while not can_calculate_24(numbers):
            numbers = [random.randint(1, 13) for _ in range(4)]

        return numbers

    def is_valid_expression(self, expression, numbers):
        '''
        判断表达式是否合法
        '''
        # 统计表达式出现的数字
        expression_numbers = [int(char) for char in re.findall(r'\d+', str(expression))]
        # 判断表达式中的数字是否与题目中的数字相同
        return sorted(expression_numbers) == sorted(numbers)

    def play_round(self):
        '''
        进行一轮游戏

        返回:
            int: 用户胜利的局数
        '''
        for _ in range(10):
            # 生成问题
            numbers= self.generate_question()
            print(f"请计算出 24：{numbers}")
            # 用户输入表达式
            user_input = input("请输入表达式：")
            # 判断用户输入是否正确
            if self.is_valid_expression(user_input, numbers) and \
                    evaluate_expression(user_input) == 24:
                print("回答正确！")
                self.win_count += 1
            else:
                print("回答错误！")

    def main(self):
        '''
        主函数
        '''
        self.play_round()
        print(f"您本轮的正确率为：{self.win_count / 10 * 100}%")

def main():
    '''
    主函数
    '''
    game = Game24()
    game.main()

if __name__ == '__main__':
    main()
