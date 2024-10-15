#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define height 100.0
#define maxium 11

int main()
{
    int n=0;double h=height;
    printf("# Input n\n");
    scanf("%d",&n);
    if(n>maxium)
        printf("No Bounce\n");
    else
    {
        for(int i=0;i<n;i++)
            h=h*2/3;
        printf("# The height pf the ball is\n%.3lf\n",h);
    }
    return 0;
}

/*
or:
int main()
{
    int n=0;int status=0;double h=height;
    printf("# Input n\n");
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        h=h*2/3;
        if(h<1)
        {
            status=1;
            break;
        }
    }
    if(status)
        printf("No Bounce\n");
    else
        printf("# The height pf the ball is\n%.3lf\n",h);
    return 0;
}

*/