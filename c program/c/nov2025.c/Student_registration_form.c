#include<stdio.h>
int main()
{
    char student_ID[10];
    char name[20];
    char Address[10];
    char Contact_number[12];
    char Email_ID[25];
    char Latest_Education[30];

    printf("please enter your student_ID: ");
    scanf("%s",&student_ID);

    printf("please enter your name: ");
    scanf(" %[^\n]",&name);

    printf("please enter your Address: ");
    scanf(" %[^\n]",&Address);

    printf("please enter your Contact_number: ");
    scanf("%s",&Contact_number);

    printf("please enter your Email_ID: ");
    scanf(" %[^\n]",&Email_ID);

    printf("please enter your Latest_Education: ");
    scanf(" %[^\n]",&Latest_Education);

    printf("\n Student_ID is: %s",student_ID);
    printf("\n Student name is: %s",name);
    printf("\n Student Address is: %s",Address);
    printf("\n Student Contact_number is: %s",Contact_number);
    printf("\n Student Email_ID is: %s",Email_ID);
    printf("\n Student Latest_Education is: %s",Latest_Education);





    return 0;
}