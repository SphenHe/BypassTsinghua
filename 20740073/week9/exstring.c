#include <stdio.h>
#include <stdlib.h>

const int Number_of_word=114514;
const int Length_of_word=30;

int main()
{
    //输入
    char *words[7]={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
    char **input=words; 	//input指向words的首地址
    char data;

    printf("# input the words");
    scanf_s("%s",&data);

    printf("Today is %s",*(input+data));
    return 0;




    //数据处理

    //输出
    return 0;
}