#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int n=0;double out=0;
    printf("# Input n\n");
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
    {
        out+=(pow(i,2)/(i+1));
    }
    printf("# The sum of the expression is\n%.3lf\n",out);
    return 0;
}