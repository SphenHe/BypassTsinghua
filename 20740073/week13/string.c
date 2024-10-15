#include<stdio.h>
#include<string.h>

struct str
{
    int length;
    int space;
    int character;
    int number;
};
struct str result;
struct str str1;
struct str str2;

void input();
void compare();
void output();
int main()
{
    input();
    compare();
    output();
    return 0;
}
void input()
{
    printf("# Please input two strings:\n");
    int c=0;
    do
    {
        c=getchar();
        str1.length++;
        if (c==' ')
            str1.space++;
        if (c>='a'&&c<='z'||c>='A'&&c<='Z')
            str1.character++;
        if (c>='0'&&c<='9')
            str1.number++;
    }
    while (c!='\n');
    str1.length--;
    do
    {
        c=getchar();
        str2.length++;
        if (c==' ')
            str2.space++;
        if (c>='a'&&c<='z'||c>='A'&&c<='Z')
            str2.character++;
        if (c>='0'&&c<='9')
            str2.number++;
    }while (c!='\n');
    str2.length--;
}
void compare()
{
    if (str1.length==str2.length)
        result.length=1;
    if (str1.space==str2.space)
        result.space=1;
    if (str1.character==str2.character)
        result.character=1;
    if (str1.number==str2.number)
        result.number=1;
    return;
}
void output()
{
    printf("# length space character number\n");
    printf("%d %d %d %d\n",result.length,result.space,result.character,result.number);
}