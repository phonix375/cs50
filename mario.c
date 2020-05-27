#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int number;
    do
    {
        //asking for the numebr from the user
        number = get_int("Height: ");
    }
    while (number < 1 || number > 8);
    int i;
    int j;
    for(i=1;i<= number;i++)
    {
        for(j=1;j <number-i+1;j++)
        {
            printf(" ");
        }
        for(j=1;j<=i;j++)
        {
            printf("#");
        }
        printf("  ");
         for(j=1;j<=i;j++)
        {
            printf("#");
        }
        printf("\n");


    }
}