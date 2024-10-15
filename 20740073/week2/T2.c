#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double a=0,h=0;
    printf("Input 2 floating-point numbers of a regular triangular prism at one time, which are the length of the base and height of side.\n");
    printf("The input of each number is separated by a space.\n");
    scanf("%lf %lf",&a,&h);
    if(a>0&&h>0)
        printf("The surface area of a regular triangular prism is %.3lf. The volume of a regular triangular prism is %.3lf.\n",3*a*h+sqrt(3)*pow(a,2)/4,h*sqrt(3)*pow(a,2)/4);
    else
        printf("The surface area of a regular triangular prism is Error. The volume of a regular triangular prism is Error.\n");
    system("pause");
    return 0;
}