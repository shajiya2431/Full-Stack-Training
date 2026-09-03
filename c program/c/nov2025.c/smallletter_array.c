#include<stdio.h>
int main()
{
    char alphabet[5][5];
    char ch='a';
    for (int i=0; i<5; i++)
    {
        for(int j=0; j<5; j++)
        {
            alphabet[i][j]=ch;
            ch++;
        }
    }
    printf("alphabet:\n\n");
    for(int i=0; i<5; i++)
    {
        for(int j=0; j<5; j++)
        {
            printf("\t%c",alphabet[i][j]);
        }
        printf("\n");
    }



   return 0;

}