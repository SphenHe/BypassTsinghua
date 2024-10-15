#include <stdio.h>
#include <math.h>

#define PRICE 10.0

int main()
{
    int n=0;double sum=0;
    printf("# Input the number of the products.\n");
    scanf("%d",&n);
    printf("# The pirce is:\n");
    if(n<0)
        printf("Error\n");
    else if(n==0)
        printf("0\n");
    else if(n<=5)
        sum=PRICE*n*(100.0-(n-1))*0.01;
    else if(n<=20)
        sum=PRICE*n*(100.0-(4+(n-5)*0.4))*0.01;
    else if(n<=50)
        sum=PRICE*n*(100.0-(10+(n-20)*0.15))*0.01;
    else if(n<=300)
        sum=PRICE*n*(100.0-(14.5+(n=50)*0.03))*0.01;
    else
        sum=PRICE*n*0.78;
    if(n>0)
        printf("%.3lf\n",sum);
    return 0;
}