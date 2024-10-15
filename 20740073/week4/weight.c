#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define weight 100

int main()
{
    int n=0;
    printf("# Input the number of weights:\n");
    scanf("%d",&n);
    int num=0;
    //x---1;y---2;z---5
    for(int z=0;z<=20;z++)
        for(int y=0;y<=(100-5*z)/2;y++)
            if((n-y-z)+2*y+5*z==100)
                num++;
    printf("# The choice of the weight is:\n%d\n",num);
    return 0;
}