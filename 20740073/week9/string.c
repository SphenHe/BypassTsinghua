#include <stdio.h>
#include <stdlib.h>

const int Length_of_s=114514;

void swap(int m, int n, int *s);

int main()
{
    //输入
    int Length=0;
    int *s;
    s=(int*)malloc(Length_of_s*sizeof(int));
    if(s==NULL)
        printf("# Error:Failed\n");
    printf("# Input the string\n");
    do
    {
        Length++;
        *(s+Length)=getchar();
    }while(*(s+Length)!='\n');
    *s=Length-1;

    //数据处理
    int m=getchar()-47;
    if(m>*s)
        printf("Error:Out of length\n");
    else if(m<*s&&m+5>*s)
        swap(m,*s,s);
    else
        swap(m,m+5,s);

    //输出
    printf("# The string after swaping is:\n");
    for (int i=1;i<=*s;i++)
        putchar(*(s+i));
    free(s);
    return 0;
}

void swap(int m, int n, int *s)
{
    while(m<n)
    {
        int temp=*(s+m);
        *(s+m)=*(s+n);
        *(s+n)=temp;
        m++;
        n--;
    }
    return;
}