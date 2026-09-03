#include<stdio.h>
int main()
{
    int count=0;
    int number[10][10];

    for(int i=0; i<10; i++)
    {
        for (int j=0; j<10; j++)
        {
        
            printf("please enter matrix number:");
            scanf("%d",&number[i][j]);

        }
        printf("\n");
    
     
    }
    for(int i=0; i<10; i++)
    {
        for(int j=0; j<10; j++)
        {
            printf("%d",number[i][j]);
        }
        printf("\n");
    }


    return 0;

}