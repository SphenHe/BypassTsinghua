#include<stdio.h>
#include<stdlib.h>

int main()
{
    //输入
    int *a,*b;
    printf("# Enter the length of the two arrays:\n");
    int m,n;
    scanf("%d %d",&m,&n);
    a=(int*)malloc(m*sizeof(int));
    b=(int*)malloc(n*sizeof(int));
    printf("# Enter the elements of the first array:\n");
    for(int i=0;i<m;i++)
        scanf("%d",a+i);
    printf("# Enter the elements of the second array:\n");
    for(int i=0;i<n;i++)
        scanf("%d",b+i);

    //合并
    int *c;
    c=(int*)malloc((m+n)*sizeof(int));
    int i=0,j=0,k=0;
    while(i<m&&j<n)
    {
        if(*(a+i)<*(b+j))
            *(c+k++)=*(a+i++);
        else
            *(c+k++)=*(b+j++);
    }
    while(i<m)
        *(c+k++)=*(a+i++);
    while(j<n)
        *(c+k++)=*(b+j++);

    //输出
    printf("# The merged array is:\n");
    for(int i=0;i<m+n;i++)
        printf("%d ",*(c+i));
    return 0;
}