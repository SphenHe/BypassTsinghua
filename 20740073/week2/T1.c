#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

int main()
{
    double AR=0,AI=0,BR=0,BI=0;
    printf("Input 4 floating-point numbers at one time, which are the real and imaginary parts of the first complex number, and the real and imaginary parts of the second complex number.\n");
    printf("The input of each number is separated by a space.\n");
    scanf("%lf %lf %lf %lf",&AR,&AI,&BR,&BI);
    double _Complex AZ=AR+AI*I;
    double _Complex BZ=BR+BI*I;
    printf("The sum of two complex numbers is:");
    printf("%.3lf%+.3lfi\n",creal(AZ+BZ),cimag(AZ+BZ));//add
    printf("The difference of two complex numbers is:");
    printf("%.3lf%+.3lfi\n",creal(AZ-BZ),cimag(AZ-BZ));//subtract
    printf("The product of two complex numbers is:");
    printf("%.3lf%+.3lfi\n",creal(AZ*BZ),cimag(AZ*BZ));//multiply
    printf("The quotient of two complex numbers is:");
    if(BR==0&&BI==0)
        printf("Error\n");
    else
        printf("%.3lf%+.3lfi\n",creal(AZ/BZ),cimag(AZ/BZ));//divide
    system("pause");
    return 0;
}