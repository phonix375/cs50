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
    for (i = 1; i <= number; i++)
    {
        //printing the number of spaces on the right
        for (j = 1; j < number - i + 1 ; j++)
        {
            printf(" ");
        }
        //printing the hashes on the left piramid
        for (j = 1; j <= i ; j++)
        {
            printf("#");
        }
        //adding the spaceing between the piramids
        printf("  ");
        for (j = 1 ; j <= i ; j++)
        {
            printf("#");
        }
        //moving to the next row
        printf("\n");


    }
}