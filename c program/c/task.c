
#include<stdio.h>
int main()
{
  int hindi;
  int english;
  int urdu;
  int math;
  int science;
  int total;
  float percentage;

  printf("please enter marks in hindi: ");
  scanf("%d",&hindi);

  printf("please enter marks in english: ");
  scanf("%d",&english);

  printf("please enter marks in urdu: ");
  scanf("%d",&urdu);

  printf("please enter marks in math: ");
  scanf("%d",&math);

  printf("please enter marks in science: ");
  scanf("%d",science);

  if(hindi<= 100 && hindi > 0)
  {
    
      if (english<= 100 && english > 0)
      {
          if(urdu<=100 && urdu > 0)
          {
             if (math<=100 && math > 0)
             {
                if (science<=100 && science > 0)
                {
                    total = hindi + english + urdu + math + science;
                    percentage = total / 5;

                    if(percentage >= 60)
                    {
                        printf("I division");

                    }
                    else if (percentage >= 45 && percentage < 60)
                    {
                        printf("II division");
                    }
                    else if (percentage >= 33 && percentage < 45)
                    {
                        printf("III division");
                    }
                    else
                    {
                        printf("failed");
                    }
                }
                else
                {
                    printf("please enter valid marks in science, marks should be b/w 1-100");
                }

             }
             else
             {
                printf("please enter valid marks in math, marks should be b/w 1-100");
             }

          }
          else
          {
              printf("please enter valid marks in urdu, marks should be b/w 1-100");
          }

          

      }
      else
      {
          printf("please enter valid marks in english, marks should be b/w 1-100");
      }
  }
  else
  {
      printf("please enter valid marks in hindi, marks should be b/w 1-100");
  }















  return 0;
}


