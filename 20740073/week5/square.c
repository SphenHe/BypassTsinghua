#include<stdio.h>
#include<math.h>

int a=0,b=0,c=0;//三组数的个数
int Count=0;//方案总数
int Status=0;//是否被标记为无效

int divide[10]={0};//分解为单个数 数字的值
int divide_used[10]={0};//判断：数是否重叠 数字 数字是否使用
int divide_count=0;//数据位数

int Storage[10][10000][10];//数据位数 第n个合法数据 数字 数字为是否使用
int Storage_count[10];//数据位数 合法数据个数n

void Input();
void List();
void Judge_num(int n);
void Combine();
void Output();

int main()
{
    List();
    Input();
    Combine();
    Output();
    return 0;
}
void Input()
{
    printf("# Input 3 numbers to devide 9 numbers into 3 pieces.\n");
    printf("# The format is \"m n p\"\n");
    scanf("%d %d %d",&a,&b,&c);
    return;
}
void Judge_num(int n)//满足则写入storage
{
    if(((int)sqrt(n))*((int)sqrt(n))==n)//完全平方数
    {
        for(int i=0;i<10;i++)//分解
        {
            divide[i]=n%10;
            n=n/10;
            divide_count++;
            if(n==0)
                break;
        }
        for(int i=0;i<divide_count;i++)
        {
            if(divide_used[divide[i]]==0)
                divide_used[divide[i]]=1;
            else
            {
                for(int j=0;j<divide_count;j++)//清零
                    divide_used[j]=0;
                divide_count=0;//清零
                return;
            }
        }
        for(int j=0;j<10;j++)
        {
            Storage[divide_count][Storage_count[divide_count]][j]=divide_used[j];//存储
            divide_used[j]=0;//清零
        }
        Storage_count[divide_count]++;//计数器
        divide_count=0;//清零
        return;
    }
    return;
}
void List()
{
    for(int i=0;i<10000000;i++)
    {
        if(i%10==1||i%10==4||i%10==5||i%10==6||i%10==9)
            Judge_num(i);
        else
            continue;
    }
    return;
}
void Combine()
{
    for(int m=1;m<=a;m++)
        for(int i=0;i<Storage_count[m];i++)
            for(int n=1;n<=b;n++)
                for(int j=0;j<Storage_count[n];j++)
                    for(int p=1;p<=c;p++)
                        for(int k=0;k<Storage_count[p];k++)
                        {
                            for(int l=0;l<10;l++)
                                if(Storage[m][i][l]+Storage[n][j][l]+Storage[p][k][l]>1)
                                    Status=1;
                            if(Status==0)
                                Count++;
                            Status=0;
                        }
    return;
}

void Output()
{
    printf("# The number of the possible cases is:\n%d\n",Count);
    return;
}
