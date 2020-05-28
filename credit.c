#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long number;
    //get input from user
    do
    {
        number = get_long("Number:");
    }
    while (number < 0);//check if the input is valid
    //create veriabels
    long i;
    int digits = 1;
    int sumeven = 0;
    int sumodd = 0;
    long tempInt;
//checks the number of digits and counts the odds and even numbers
    for (i = 10; number / i >= 1 ; i *= 10)
    {
        //check if the number is even
        if (digits % 2 == 0)
        {
            tempInt = ((number % i) / (i / 10)) * 2;
            sumeven += (tempInt % 10) + (tempInt - (tempInt % 10)) / 10;
        }
        //check if the number is even
        else
        {
            sumodd += (number % i) / (i / 10);
        }
        digits++;
        if (number / (i * 10) <= 1)
        {
            if (digits % 2 == 0)
            {
                tempInt = (number / i) * 2;
                sumeven += (tempInt % 10) + (tempInt - (tempInt % 10)) / 10;
            }
            else
            {
                sumodd += number / i;

            }
        }

    }
    //cheks if the sum is correct
    if ((sumeven + sumodd) % 10 == 0)
    {
        //cheks the first digits of the number
        long start = number;
        while (start > 100)
        {
            start /= 10;
        }
        //cheks if american
        if (start == 34 || start == 37)
        {
            if (digits == 15)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        //cheks if mastercard
        else if (start > 50 && start < 56)
        {
            if (digits == 16)
            {
                printf("MASTERCARD\n");
            }
            else
            {
                //prints if the card if not valid
                printf("INVALID\n");
            }
        }
        else
        {
            //cheks if VISA
            if (4 == (start - (start % 10)) / 10 && digits >= 13 && digits <= 16)
            {
                printf("VISA\n");
            }
            else
            {
                //prints if the card if not valid
                printf("INVALID\n");
            }

        }

    }
    else
    {
        //prints if the card if not valid
        printf("INVALID\n");
    }
}