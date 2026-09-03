#include<stdio.h>
int main()
{
    char name[5][20];
    char address[5][30];
    char email[5];
    int i;
    for(int i=0; i<5; i++);
    {
        printf("how many student enter");
        scanf("%d",&i[i]);

        printf(" enter student name");
        scanf(" %[^\n]",&name[i]);

        printf("enter student address");
        scanf(" %s",&address[i]);

        printf("enter student email");
        scanf(" %[^\n]",&emai[i]);


    }

    

    printf("\n Student name is: %s",name);
    printf("\n Student address is: %s",address);
    printf("\n Student contact is: %s",contact);


    return 0;
}