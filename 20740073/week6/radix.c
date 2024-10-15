#include <stdio.h>

int main()
{
    int Input=0;
    int Input_Storage=0;
    int Storage_8[1000]={0};
    int Storage_16[1000]={0};
    int Count=0;
    int Status=0;
    printf("# Input your number:\n");
    do
    {
        Status=0;
        scanf("%d",&Input);
        if(Input<=0)
        {
            printf("# Error, please input again:\n");
            Input=0;
            Status=1;
        }
    }while(Status==1);
    Input_Storage=Input;
    do
    {
        Storage_8[Count]=Input%8;
        Input=Input/8;
        Count++;
    } while (Input!=0);
    printf("# Convert the number to octal, the value is\n0");
    for(int i=Count-1;i>=0;i--)
        printf("%d",Storage_8[i]);
    printf("\n");
    Input=Input_Storage;
    Count=0;
    do
    {
        Storage_16[Count]=Input%16;
        Input=Input/16;
        Count++;
    } while (Input!=0);
    printf("# Convert the number to hexadecimal, the value is\n0x");
    for(int i=Count-1;i>=0;i--)
        if(Storage_16[i]<10)
            printf("%d",Storage_16[i]);
        else switch (Storage_16[i])
        {
            case 10:
                printf("a");
                break;
            case 11:
                printf("b");
                break;
            case 12:
                printf("c");
                break;
            case 13:
                printf("d");
                break;
            case 14:
                printf("e");
                break;
            case 15:
                printf("f");
                break;
        }
    printf("\n");
    return 0;
}