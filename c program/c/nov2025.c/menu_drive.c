#include<stdio.h>
int main()
{

    int  choice,a,b;
    do
    {
        printf("******* menu_drive*******");
        printf("Add\n");
        printf("Subtract\n");
        printf("Multiply\n");
        printf("Divide\n");
        printf("Exit\n");

        printf("Enter your choice");
        scanf("%d",&choice);

        if(choice >=1 && choice<= 5)
        {
            printf("Enter first number: ");
            scanf("%d",&a);

            printf("enter second number:");
            scanf("%d",&b);
        }
        if(choice == 1)
        {
            printf("your selected add= %d\n",a+b);
        }
        else if(choice == 2)
        {
            printf("your selected subtraction= %d\n",a-b);
        }
        else if(choice ==3)
        {
            printf("your selected multiply= %d\n",a*b);
        }
        else if(choice ==4)
        {
             printf("your selected divide= %d\n",a/b);
        }
        else
        {
            printf("exited...\n");
        }
    

    
      
        

        
      
    }
    while(choice<5);
    









    return 0;


}
    
        