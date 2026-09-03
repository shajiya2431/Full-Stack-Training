#include<stdio.h>
int main()
{
    int Hindi;
    int English;
    int count=0;


do
{
    printf("please enter Hindi marks:");
    scanf("%d",&Hindi);
    
    printf("please enter English marks:");
    scanf("%d",&English);
    
    int total = Hindi+English;
    float percentage=total/2;
    if(percentage>90 && 100<percentage)
    {
        printf("you have cleared the upsc exam");
        break;
    }
    else
    {
        printf("\n you have failed , please try again");
        count++;
        
        
        

        
    }

}
while(count<5);

    return 0;




}