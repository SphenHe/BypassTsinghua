#include<stdio.h>

int main()
{
    int a=0,b=0;
    printf("# Please input the lenth and width of the martix\n");
    scanf("%d %d",&a,&b);
    int matrix[a][b];
    printf("# Please input the martix\n");
    for(int i=0;i<a;i++)
        for(int j=0;j<b;j++)
            scanf("%d",&matrix[i][j]);
    printf("# The martix after transpose is:\n");
    for(int i=0;i<b;i++)
    {
        for(int j=0;j<a;j++)
            printf("%d ",matrix[j][i]);
        printf("\n");
    }
    return 0;
}