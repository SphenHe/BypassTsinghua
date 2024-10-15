// Caesar cipher

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc!=4)
    {
        printf("# Usage: passwd.in passwd.out delta\n");
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
    char name[1000];
    char passwd[1000];
    int delta=atoi(argv[3]);
    while(fgets(line,1000,in)!=NULL)
    {
        sscanf(line,"{\"username\":\"%[^\"]\",\"password\":\"%[^\"]\"}",name,passwd);
        for(int i=0;i<strlen(passwd);i++)
        {
            if(passwd[i]>='!'&&passwd[i]<='}')
            {
                passwd[i]+=delta;
                if(passwd[i]>'}')
                    passwd[i]-=94;
            }
        }
        fprintf(out,"{\"username\":\"%s\",\"password\":\"%s\"}\n",name,passwd);
    }

    fclose(in);
    fclose(out);
    return 0;
}