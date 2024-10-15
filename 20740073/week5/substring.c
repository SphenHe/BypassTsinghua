#include<stdio.h>

int InStr[1001];
int SearchStr[1001];

int LenIn=0;
int LenSearch=0;

int Status=0;
int Count[1001];
int CountNum=0;

void Input();
void Search();
void Output();

int main()
{
    Input();
    Search();
    Output();
    return 0;
}

void Input()
{
    printf("# Input 2 strings.\n");
    do
    {
        InStr[LenIn]=getchar();
        LenIn++;
    }while(InStr[LenIn-1]!=10);
    do
    {
        SearchStr[LenSearch]=getchar();
        LenSearch++;
    }while(SearchStr[LenSearch-1]!=10);
    LenIn--;
    LenSearch--;
    return;
}

void Search()
{
    for(int i=0;i<LenIn-LenSearch+1;i++)
    {
        for(int j=0;j<LenSearch&&Status==0;j++)
        {
            if(InStr[i+j]!=SearchStr[j])
            {
                Status=1;
                break;
            }
        }
        if(Status==0)
        {
            Count[CountNum]=i;
            CountNum++;
        }
        Status=0;
    }
    return;
}

void Output()
{
    printf("# The number of the substring is:\n%d\n",CountNum);
    printf("# The location of the substring is:\n");
    for(int i=0;i<CountNum;i++)
        printf("%d\n",Count[i]);
    return;
}