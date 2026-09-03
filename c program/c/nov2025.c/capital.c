#include<stdio.h>
int main()
{
    char A[5][6];
    char alphabet;
    printf("enter alphabet");
    scanf("\t%c" ,&alphabet);
    for(int i=0; i<5; i++)
    {
        for(int j=0; j<5; j++)
        {
            printf("\t%c",A[i][j]=alphabet);
            alphabet++;
            
        }
        printf("\n");
    }


    return 0;

}