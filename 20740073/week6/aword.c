#include<stdio.h>

int max=0;
int memory[1000][1000]={0};
int is_available[1000]={0};
int memory_lenth[1000]={0};
int word_count=0;
int word_lenth=0;

int main()
{
    int c=0;
    //读取输入
    printf("# Please input a sentence:\n");
    while(c!=EOF&&c!='\n')
    {
        c=getchar();
        memory[word_count][word_lenth]=c;
        word_lenth++;
        if(c=='a'||c=='A')
        {
            is_available[word_count]=1;
        }
        if(c==' '||c=='\n'||c==EOF)
        {
            memory_lenth[word_count]=word_lenth;
            if(is_available[word_count]==1)
                if(word_lenth>max)
                    max=word_lenth;
            word_count++;
            word_lenth=0;
        }
    }
    //分析输入
    printf("# The longest word that contain a or A is:\n");
    if(max==0)
        printf("Error\n");
    else
        for(int i=0;i<word_count;i++)
            if(is_available[i]==1&&memory_lenth[i]==max)
            {
                for(int j=0;j<memory_lenth[i];j++)
                    putchar(memory[i][j]);
                putchar('\n');
            }
    return 0;
}