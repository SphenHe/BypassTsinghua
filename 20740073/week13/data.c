#include<stdio.h>
#include<string.h>

struct date
{
    int year;
    int month;
    int day;
    int febday;
    int count;
};

struct date date1;
struct date date2;

void input();
void count();

int main()
{
    input();
    count();
    printf("# The difference between %d %d %d and %d %d %d is: \n%d\n",date1.year,date1.month,date1.day,date2.year,date2.month,date2.day,date2.count-date1.count);
    return 0;
}

void input()
{
    printf("# Please input two dates:\n");
    scanf("%d %d %d",&date1.year,&date1.month,&date1.day);
    scanf("%d %d %d",&date2.year,&date2.month,&date2.day);
    if ((date1.year%4==0&&date1.year%100!=0)||date1.year%400==0)
        date1.febday=29;
    else
        date1.febday=28;
    if ((date2.year%4==0&&date2.year%100!=0)||date2.year%400==0)
        date2.febday=29;
    else
        date2.febday=28;
    if (date1.year<2000||date1.month<0||date1.day<0||date2.year<2000||date2.month<0||date2.day<0||date1.month>12||date2.month>12||date1.day>31||date2.day>31)
        printf("# Wrong Input!\n");
    else if ((date1.month==2&&date1.day>date1.febday)||(date2.month==2&&date2.day>date2.febday))
        printf("# Wrong Input!\n");
    else if (((date1.month==4||date1.month==6||date1.month==9||date1.month==11)&&date1.day>30)||((date2.month==4||date2.month==6||date2.month==9||date2.month==11)&&date2.day>30))
        printf("# Wrong Input!\n");
    else if (date1.year==date2.year&&date1.month==date2.month&&date1.day==date2.day)
        printf("# Wrong Input: %d %d %d is the same day as %d %d %d\n",date1.year,date1.month,date1.day,date2.year,date2.month,date2.day);
    else if (date1.year>date2.year||(date1.year==date2.year&&date1.month>date2.month)||(date1.year==date2.year&&date1.month==date2.month&&date1.day>date2.day))
        printf("# Wrong Input: %d %d %d is earlier than %d %d %d\n",date2.year,date2.month,date2.day,date1.year,date1.month,date1.day);
}
void count()
{
    for (int i=2000;i<date1.year;i++)
    {
        if ((i%4==0&&i%100!=0)||i%400==0)
            date1.count+=366;
        else
            date1.count+=365;
    }
    for (int i=1;i<date1.month;i++)
    {
        if (i==2)
            date1.count+=date1.febday;
        else if (i==4||i==6||i==9||i==11)
            date1.count+=30;
        else
            date1.count+=31;
    }
    date1.count+=date1.day;
    for (int i=2000;i<date2.year;i++)
    {
        if ((i%4==0&&i%100!=0)||i%400==0)
            date2.count+=366;
        else
            date2.count+=365;
    }
    for (int i=1;i<date2.month;i++)
    {
        if (i==2)
            date2.count+=date2.febday;
        else if (i==4||i==6||i==9||i==11)
            date2.count+=30;
        else
            date2.count+=31;
    }
    date2.count+=date2.day;
    return;
}