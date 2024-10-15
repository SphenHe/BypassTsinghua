#include<stdio.h>

int memory_all[1000]={0};
int memory_lenth=0;
int state=0;
int main()
{
    int c=0;
    int memory=0;
    printf("# Please input a sentence:\n");
    while(c!=EOF&&c!='\n')
    {
        c=getchar();
        if(memory=='i'&&c=='s')
        {
            memory_all[memory_lenth]='b';
            memory_lenth++;
            memory='e';
            state=1;
        }
        else
        {
            memory_all[memory_lenth]=memory;
            memory_lenth++;
            memory=c;
        }
    }
    printf("# The sentence after being is:\n");
    if(state==1)
        for(int i=0;i<memory_lenth;i++)
            putchar(memory_all[i]);
    else
        printf("Error\n");
    return 0;
}