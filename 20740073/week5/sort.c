#include<stdio.h>

int Ascii[128];
int main()
{
    //input
    int Char=0,Count=0;
    do
    {
        Char=getchar();
        if(Char>=97&&Char<=122)
            Ascii[Char-32]=1;
        else
            Ascii[Char]=1;
    }while(Char!=10);

    //output
    for(int i=48;i<58;i++)
        if(Ascii[i])
        {
            putchar(i);
            putchar(10);
        }
    for(int i=65;i<91;i++)
        if(Ascii[i])
        {
            putchar(i);
            putchar(10);
        }
    return 0;
}