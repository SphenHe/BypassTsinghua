#include<stdio.h>
#include<math.h>

int main()
{
    int inf=0,sup=0;
    printf("# Please input the range of the prime you want to find\n");
    printf("# The range is inf to sup\n");
    do
    {
        scanf("%d %d",&inf,&sup);
        if(inf>=sup||inf<0||sup<0)
        {
            printf("# The range is inf to sup\n");
            printf("# Please input again\n");
            inf=0;sup=0;
        }
    }while(inf>=sup||inf<0||sup<0);
    //质数打表
    int prime[sup+1];prime[1]=2;int count=1;
    int sto[sup+1];int stocount=0;
    if(inf<2)
    {
        sto[stocount]=2;
        stocount++;
    }
    for (int j=3;j<sup;j+=2)
    {
        for(int k=1;k<=count;k++)
        {
            if(j%prime[k]==0)
                break;
            else if(k==count)
            {
                count++;
                prime[count]=j;
                if(j>inf)
                {
                    sto[stocount]=j;
                    stocount++;
                }
                break;
            }
        }
    }
    if(stocount==0)
        printf("# Error\n");
    else
    {
        printf("# The number of prime numbers in the range is\n%d\n# They are\n",stocount);
        for(int i=0;i<stocount;i++)
            printf("%d\n",sto[i]);
    }
    return 0;
}