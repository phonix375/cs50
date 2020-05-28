#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number;
    do
    {
        number = get_long("Number:");
    }
    while(number < 0);
    long i;
    int digits = 1;
    int sumeven = 0;
    int sumodd =0;
    long tempInt;

    for (i = 10; number / i >= 1 ; i *= 10)
    {

        if(digits % 2 == 0)
        {
            tempInt = ((number % i) / (i/10)) * 2;
            sumeven += (tempInt % 10) +  (tempInt - (tempInt % 10)) / 10;
        }
        else
        {
            sumodd += (number % i) / (i/10);
        }
        digits++;
        if(number / (i*10) <= 1 )
        {
            if(digits % 2 == 0)
            {
                tempInt = (number / i) * 2;
                sumeven += (tempInt % 10) +  (tempInt - (tempInt % 10)) / 10;
            }
            else
            {
                sumodd += number / i;

            }
        }

    }
    if ((sumeven + sumodd) % 10 == 0)
    {
        long start = number;
        while (start > 100)
        {
            start /= 10;
        }
        if (start == 34 || start == 37)
        {
            if(digits == 15)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (start >50 && start < 56)
        {
            if(digits == 16)
            {
                printf("MASTERCARD\n");
            }
            else
            {
               printf("INVALID\n");
            }
        }
        else
        {
            if(4 == (start - (start % 10)) / 10 && digits >= 13 && digits <= 16 )
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }

        }

    }
    else
    {
        printf("INVALID\n");
    }
}