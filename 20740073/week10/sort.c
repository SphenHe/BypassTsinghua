/*
** Use six different ways to sort an array of integers
** Compare the time of each method
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

clock_t start, end;

int N;
int *input;
int *in;

void ResetArray();
void PrintArray();

void Bubble();
void Selection();
void Insertion();
void Shell();
void Merge();
void Quick();

void MergeSort(int left, int right);
void MergeArray(int left, int mid, int right);

void QuickSort(int left, int right);

int main()
{
    printf("# --------------------------------------------------------\n");
    printf("# Please input the number of integers: ");
    scanf("%d", &N);
    input=(int *)malloc(N*sizeof(int));
    printf("# --------------------------------------------------------\n");
    printf("# Please input the integers: ");
    for(int i=0;i<N;i++)
        scanf("%d", input+i);
    in=(int *)malloc(N*sizeof(int));
    printf("# --------------------------------------------------------\n");

    printf("# The original array is:\n# ");
    for(int i=0;i<N;i++)
        printf("%d ", *(input+i));
    printf("\n");

    Bubble();
    Selection();
    Insertion();
    Shell();
    Merge();
    Quick();

    printf("# --------------------------------------------------------\n");
    free(input);
    free(in);
    return 0;
}

void ResetArray()
{
    for(int i=0;i<N;i++)
        *(in+i)=*(input+i);
    return;
}
void PrintArray()
{
    printf("# The sorted array is:\n # ");
    for(int i=0;i<N;i++)
        printf("%d ", *(in+i));
    printf("\n");
    return;
}

void Bubble()
{
    ResetArray();
    start=clock();
    for(int i=0;i<N;i++)
        for(int j=0;j<N-i-1;j++)
            if(*(in+j)>*(in+j+1))
            {
                int temp=*(in+j);
                *(in+j)=*(in+j+1);
                *(in+j+1)=temp;
            }
    end=clock();
    printf("# --------------------------------------------------------\n");
    printf("# Bubble sort:\n");
    PrintArray();
    printf("# Time cost: %lf\n", (double)(end-start)/CLOCKS_PER_SEC);
    return;
}
void Selection()
{
    ResetArray();
    start=clock();
    int min;
    for(int i=0;i<N;i++)
    {
        min=i;
        for(int j=i+1;j<N;j++)
            if(*(in+j)<*(in+min))
                min=j;
        int temp=*(in+i);
        *(in+i)=*(in+min);
        *(in+min)=temp;
    }
    end=clock();
    printf("# --------------------------------------------------------\n");
    printf("# Selection sort:\n");
    PrintArray();
    printf("# Time cost: %lf\n", (double)(end-start)/CLOCKS_PER_SEC);
    return;
}
void Insertion()
{
    ResetArray();
    start=clock();
    int temp;
    for(int i=1;i<N;i++)
    {
        temp=*(in+i);
        int j=i-1;
        while(j>=0 && *(in+j)>temp)
        {
            *(in+j+1)=*(in+j);
            j--;
        }
        *(in+j+1)=temp;
    }
    end=clock();
    printf("# --------------------------------------------------------\n");
    printf("# Insertion sort:\n");
    PrintArray();
    printf("# Time cost: %lf\n", (double)(end-start)/CLOCKS_PER_SEC);
    return;
}
void Shell()
{
    ResetArray();
    start=clock();
    int temp;
    for(int gap=N/2;gap>0;gap=gap/2)
        for(int i=gap;i<N;i++)
        {
            temp=*(in+i);
            int j=i-gap;
            while(j>=0 && *(in+j)>temp)
            {
                *(in+j+gap)=*(in+j);
                j-=gap;
            }
            *(in+j+gap)=temp;
        }
    end=clock();
    printf("# --------------------------------------------------------\n");
    printf("# Shell sort:\n");
    PrintArray();
    printf("# Time cost: %lf\n", (double)(end-start)/CLOCKS_PER_SEC);
    return;
}
void Merge()
{
    ResetArray();
    start=clock();
    MergeSort(0, N-1);
    end=clock();
    printf("# --------------------------------------------------------\n");
    printf("# Merge sort:\n");
    PrintArray();
    printf("# Time cost: %lf\n", (double)(end-start)/CLOCKS_PER_SEC);
    return;
}
void Quick()
{
    ResetArray();
    start=clock();
    QuickSort(0, N-1);
    end=clock();
    printf("# --------------------------------------------------------\n");
    printf("# Quick sort:\n");
    PrintArray();
    printf("# Time cost: %lf\n", (double)(end-start)/CLOCKS_PER_SEC);
    return;
}

void MergeSort(int left, int right)
{
    if(left<right)
    {
        int mid=(left+right)/2;
        MergeSort(left, mid);
        MergeSort(mid+1, right);
        MergeArray(left, mid, right);
    }
    return;
}
void MergeArray(int left, int mid, int right)
{
    int i=left, j=mid+1, k=left;
    while(i<=mid && j<=right)
    {
        if(*(in+i)<*(in+j))
            *(input+k++)=*(in+i++);
        else
            *(input+k++)=*(in+j++);
    }
    while(i<=mid)
        *(input+k++)=*(in+i++);
    while(j<=right)
        *(input+k++)=*(in+j++);
    for(int i=left;i<=right;i++)
        *(in+i)=*(input+i);
    return;
}

void QuickSort(int left, int right)
{
    if(left<right)
    {
        int i=left, j=right, temp=*(in+left);
        while(i<j)
        {
            while(i<j && *(in+j)>=temp)
                j--;
            if(i<j)
                *(in+i++)=*(in+j);
            while(i<j && *(in+i)<=temp)
                i++;
            if(i<j)
                *(in+j--)=*(in+i);
        }
        *(in+i)=temp;
        QuickSort(left, i-1);
        QuickSort(i+1, right);
    }
    return;
}