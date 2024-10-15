#include <stdio.h>

int main()
{
    int num=0;int temp=0;
    printf("# Input your number:\n");
    do
    {
        temp=getchar();
        if(temp==49)
            num++;
    }while(temp!=EOF);
    printf("# The frequnency of \"1\" is \n%d\n",num);
    return 0;
}