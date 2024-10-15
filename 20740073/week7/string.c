#include<stdio.h>

int main()
{
    int Nun_n=0;
    int Cha_n=0;
    int c=0;
    printf("# 请输入一串字符:\n");
    do
    {
        c=getchar();
        if(c>='0'&&c<='9')
        {
            Nun_n++;
        }
        else if(c>='e'&&c<='k')
        {
            Cha_n++;
        }
    }while(c!='\n'&&c!='\0'&&c!=' ');
    printf("# 数字个数为:\n%d\n",Nun_n);
    printf("# e到k之间的字母个数为:\n%d\n",Cha_n);
    return 0;
}