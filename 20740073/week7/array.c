/*
**唔，这道题还可以直接推出表达式，懒得推了
*/

#include<stdio.h>

int F(int x);
int G(int x);

int main()
{
    printf ("# 请输入一个整数:\n");
    int x=0;
    scanf ("%d",&x);
    printf ("# F(%d)=\n%d\n",x,F(x));
    printf ("# G(%d)=\n%d\n",x,G(x));
    return 0;
}

int F(int x)
{
    switch (x)
    {
        case 0:
            return 1;
        case 1:
            return 2;
        default:
            return (2*F(x-1)+F(x-2))%10000019;
    }
}
int G(int x)
{
    switch (x)
    {
        case 0:
            return 0;
        case 1:
            return 1;
        default:
            return (G(x-1)+2*G(x-2))%10000019;
    }
}


