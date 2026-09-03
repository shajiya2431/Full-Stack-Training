#include<stdio.h>
int main()
{
    int number[10];
    int greatest;
    int smallest;

    for(int i=0; i<10; i++)
    {
        printf("enter number");
        scanf("%d",&number[i]);

    }
    greatest = number[0];
    smallest = number[0];
    for(int i=1; i<10; i++)
    {
        if(number[i]>greatest)
        greatest = number[i];

        if(number[i]<smallest)
        smallest = number[i];
    }
    printf("greatest number=%d\n",greatest);
    printf("smallest number=%d\n",smallest);





    return 0;

}