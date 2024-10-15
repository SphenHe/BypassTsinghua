#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// replace the include with the header file
// run sample : header helloworld.h helloworld.txt
// input: helloworld.h
// output: helloworld.txt
// myheader.h is the header file

// sample:

// sample helloworld.c
// #include <myheader.h>
// int main(){
//     return 0;
// }

// sample myheader.h
// void f(){
//     return;
// }

// sample helloworld.txt
// void f(){
//     return;
// }
// int main(){
//     return 0;
// }

int main(int argc, char *argv[])
{
    if(argc!=3)
    {
        printf("# Usage: %s <input> <output>\n",argv[0]);
        exit(1);
    }

    FILE *in=fopen(argv[1],"r");
    FILE *out=fopen(argv[2],"w");
    if (in == NULL)
    {
        printf("# Can't open file %s\n",argv[1]);
        exit(1);
    }
    if (out == NULL)
    {
        printf("# Can't open file %s\n",argv[2]);
        exit(1);
    }

    char line[1000];
    char include[1000];
    while(fgets(line,1000,in)!=NULL)
    {
        if(line[0]=='#')
        {
            sscanf(line,"#include <%[^>]>",include);
            sscanf(line,"#include \"%[^\"]\"",include);
            FILE *header=fopen(include,"r");
            if(header==NULL)
            {
                printf("# Can't open file %s\n",include);
                exit(1);
            }
            char headerline[1000];
            while(fgets(headerline,1000,header)!=NULL)
            {
                fprintf(out,"%s",headerline);
            }
            fclose(header);
        }
        else
        {
            fprintf(out,"%s",line);
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}