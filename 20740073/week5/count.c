#include <stdio.h>

int Count=0;int Input=1;
int m=0,n=0;
int Location_x=0,Location_y=0;

int Square[1001][1001];
int Status[1000001];

void dfs();
void Action(int k);
void Write(int k);
void ReWrite(int k);
void LocationPlus();
void LocationReduce();

int main()
{
    printf("# Input 2 numbers, which are the length and width of the square.\n");
    printf("# The format is \"a b\"\n");
    while(Input)
    {
        scanf("%d %d",&m,&n);
        if(m<=0||n<=0)
            printf("# Wrong input, please input agian.\n");
        else
            Input=0;
    }

    dfs();
    printf("# The number of the choice is:\n%d\n",Count);
    return 0;
}

void dfs()
{
    for(int k=m*n;k>0;k--)
    {
        if(Status[k]==0)
        {
            if(k==1&&Location_x==m-1&&Location_y==n-1)//数完了！
            {
                Count++;
                return;
            }
            if(Location_x==0||Location_y==0)//边界线
            {
                if(Location_x==0&&Location_y==0)//原点
                    Action(k);
                else if(Location_x==0&&k<Square[Location_x][Location_y-1])//第一行
                    Action(k);
                else if(Location_y==0&&k<Square[Location_x-1][Location_y])//第一列
                    Action(k);
            }
            else if(k<Square[Location_x-1][Location_y]&&k<Square[Location_x][Location_y-1])//正常位置
                Action(k);
        }
    }
    return;
}
void Action(int k)
{
    Write(k);
    dfs();
    ReWrite(k);
}
void Write(int k)
{
    Square[Location_x][Location_y]=k;
    Status[k]=1;
    LocationPlus();
    return;
}
void ReWrite(int k)
{
    Square[Location_x][Location_y]=0;
    Status[k]=0;
    LocationReduce();
    return;
}
void LocationPlus()
{
    Location_x++;
    if(Location_x>=m)
    {
        Location_x=0;
        Location_y++;
    }
    return;
}
void LocationReduce()
{
    Location_x--;
    if(Location_x<0)
    {
        Location_x=m-1;
        Location_y--;
    }
    return;
}
