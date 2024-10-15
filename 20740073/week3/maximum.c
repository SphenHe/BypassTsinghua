#include <stdio.h>
#include <math.h>

int compare(double, double);
double absd(double);
int main()
{
    double a=0,b=0,c=0,d=0,max=0;
    printf("# Input 4 floating-point numbers at one time.\n");
    printf("# The input of each number is separated by a space.\n");
    scanf("%lf %lf %lf %lf",&a,&b,&c,&d);

    if(compare(a,0)==0&&compare(b,0)==0&&compare(c,0)==0&&compare(d,0)==0)
    {
        printf("Exit\n");
        goto end;
    }
    if(compare(a,b)*compare(a,c)*compare(a,d)*compare(b,c)*compare(b,d)*compare(c,d)==0)
    {
        printf("Error:Equal\n");
        goto end;
    }
    if(compare(a,1000)==1||compare(b,1000)==1||compare(c,1000)==1||compare(d,1000)==1||compare(a,-1000)==-1||compare(b,-1000)==-1||compare(c,-1000)==-1||compare(d,-1000)==-1)
    {
        printf("Error:Out of Range\n");
        goto end;
    }

    max=a;
    if(compare(b,max)>0)
        max=b;
    if(compare(c,max)>0)
        max=c;
    if(compare(d,max)>0)
        max=d;

    printf("# Max of the 4 floating-point numbers is:\n");
    printf("%.3lf\n",max);

    end:
    return 0;
}

int compare(double a, double b)
{
    double delta=(a-b)/(absd(a)+absd(b)+1e-100);
    if(delta>-1e-10&&delta<1e-10)
        return 0;
    else if(delta>0)
        return 1;
    else if(delta<0)
        return -1;
    return 114514;
}
double absd(double x)
{
    if (x>0)
        return x;
    else
        return -x;
}