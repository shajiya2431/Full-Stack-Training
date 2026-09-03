#include<stdio.h>
int main()
{
    int number[10]={2,6,5,-7,-6,9,-10,4,-12,-5};
    printf("\npositive number:");
    
    for(int i=0; i<10; i++)
    {
        if(number[i]>0)
        {
            printf("\n%d",number[i]);
        }
    }
    printf("\nnegative number:");
    for(int i=0; i<10; i++)
    {
        if(number[i]<0)
        {
            printf("\n%d",number[i]);
        }
    }





    return 0;

}