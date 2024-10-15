#include<stdio.h>
#include<stdlib.h>

const int Number_of_words=1145;
const int Length_of_word=30;

int main()
{
    //malloc
    int Count=0;int flag=0;
    int **a;
    a=(int **)malloc(Number_of_words*sizeof(int *));
    if(a==NULL)
    {
        printf("# Memory allocation of **a failed.\n");
        return -1;
    }
    for(int i=0;i<Number_of_words;i++)
    {
        *(a+i)=(int *)malloc(Length_of_word*sizeof(int));
        if(*(a+i)==NULL)
        {
            printf("# Memory allocation of *(a+%d)failed.\n",i);
            return -1;
        }
    }
    //输入
    printf("# Input the words:\n");
    for(int i=0;i<Number_of_words;i++)
    {
        for(int j=0;j<Length_of_word;j++)
        {
            *(*(a+i)+j)=getchar();
            if(j==0)
                *(*(a+i)+j)-=32;
            if(*(*(a+i)+j)==' ')
            {
                *(*(a+i)+j)='\0';
                break;
            }
            if(*(*(a+i)+j)=='\n')
            {
                *(*(a+i)+j)='\0';
                flag=1;
                break;
            }
        }
        Count++;
        if(flag==1)
            break;
    }
    //输出
    printf("# Output:\n");
    for(int i=Count-1;i>=0;i--)
    {
        for(int j=0;j<Length_of_word;j++)
        {
            if(*(*(a+i)+j)=='\0')
                break;
            putchar(*(*(a+i)+j));
        }
        putchar(' ');
    }
    //free
    for(int i=0;i<Number_of_words;i++)
        free(*(a+i));
    free(a);

    return 0;
}
