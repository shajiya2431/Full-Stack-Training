#include<stdio.h>
int main()
{
     int companyotp 6677;
     int userotp;

     printf("please enter otp: ");
     scanf("%d", userotp );

     if(companyotp--userotp)
     {
        printf("\nmatched: otp verified successfully ");

     }
     
     
     return 0;
}