#include<stdio.h>
int main()
{
    int hindi;
    int urdu;
    int english;
    int math;
    int science;
    int total;
    float percentage;
    printf("please enter marks in hindi: ");
    scanf("%d",&hindi);

    printf("please enter marks in urdu: ");
    scanf("%d",&urdu);

    printf("please enter marks in english: ");
    scanf("%d",&english);

    printf("please enter marks in math: ");
    scanf("%d",&math);

    printf("please enter marks in science: ");
    scanf("%d",&science);

    total=hindi+urdu+english+math+science;
    percentage=total/5;

    

    if(percentage>=60)
    {
        printf("I division");

    }
    else if(percentage>=45 && percentage<60)
    {
        printf("II division ");
    
    }
    else if (percentage>=33 && percentage<45)
    {
        printf("III division ");
    }
    else 
    {
        printf("failed");
    }

    return 0;


}