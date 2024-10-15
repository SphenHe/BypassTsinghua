#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define Pi 3.14159265358979324
#define anglea Pi/6
#define angle 0.523598776
#define maxium 21

long long int Factorial(long long int x);

int main()
{
    long double output=0;long double delta=0;
    for (int i=1;i<maxium;i+=2)
    {
        delta=pow(angle,i)/Factorial(i);
        if((i-1)%4)
            delta=-delta;
        output+=delta;
    }
    printf("# sin30=\n%.3Lf\n",output);
    return 0;
}

long long int Factorial(long long int x)
{
    if(x)
        return x*Factorial(x-1);
    return 1;
}