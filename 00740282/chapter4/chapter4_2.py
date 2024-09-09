'''
编写函数 is_word_palindrome()，判断某个给定的英文字符串是否为单词回文。
实际处理时，忽略所有非英文单词内容。
所谓单词回文是指，正读与倒读时，其中单词及它们的次序完全一致的字符串。
'''

def is_word_palindrome(s):
    '''
    判断是否为单词回文

    '''
    # 仅保留英文单词
    s = ''.join([c for c in s if c.isalpha() or c.isspace()])

    # 判断是否为回文
    words = s.split()
    # 仅比对一半即可
    for i in range(len(words)//2):
        if words[i] != words[-1-i]:
            return False
    return True

def main():
    '''
    主函数

    说明：
    通过调用 is_word_palindrome() 函数判断用户输入的字符串是否为单词回文。
    '''
    s = input('请输入字符串：')
    if is_word_palindrome(s):
        print('是单词回文')
    else:
        print('不是单词回文')

if __name__ == '__main__':
    main()
