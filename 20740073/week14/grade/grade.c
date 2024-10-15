#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAX_STUDENT = 10;
const int MAX_NAME = 20;

struct student
{
    int id;
    int score;
};
struct student stu[MAX_STUDENT];

int main()
{
    FILE *in = fopen("grade.in", "r");
    if (in == NULL)
    {
        printf("Can't open file grade.in\n");
        exit(1);
    }
    int i = 0;
    while (fscanf(in, "{\"id\":%d,\"grade\":%d}\n", &stu[i].id, &stu[i].score) != EOF)
        i++;
    fclose(in);

    FILE *out = fopen("grade.out", "w");
    if (out == NULL)
    {
        printf("Can't open file grade.out\n");
        exit(1);
    }
    for(int j = 0; j < i; j++)
        if(stu[j].score < 90 && stu[j].score > 80)
        {
            fprintf(out,"{\"id\":%d,\"grade\":%d}\n", stu[j].id, stu[j].score);
        }
    fclose(out);

    return 0;
}