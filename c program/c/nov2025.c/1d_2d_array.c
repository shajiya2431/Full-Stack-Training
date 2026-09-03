#include<stdio.h>
int main()
{ 
    char student_ID[5][15];
    char student_name[5][20];
    long long int student_contact[5];
    char student_Address[5][40];
    char student_latest_education[5][10];
    
    int i;
    for(int i=0; i<5; i++);
    {
        printf("Enter student_ID: ");
        scanf(" %[^\n]",&student_ID[i]);

        printf("Enter student_name: ");
        scanf(" %[^\n]",&student_name[i]);

        printf("Enter student_contact: ");
        scanf("%lld",&student_contact[i]);

        printf("Enter student_Address: ");
        scanf(" %[^\n]",&student_Address[i]);

        printf("Enter student_latest_education: ");
        scanf(" %[^\n]",&student_latest_education[i]);

    }


    for(int k = 0; k < 5; k++)
    {
        printf("student_ID   : %s\n",student_ID[k]);
        printf("student_name   : %s\n",student_name[k]);
        printf("student_contact   : %lld\n",student_contact[k]);
        printf("student_Address: %s\n",student_Address[k]);
        printf("student_latest_education: %s\n",student_latest_education[k]);

       

    }

    return 0;
}


