#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
int main(void)
{
    string text = get_string("TEXT: ");
    //createing the veriables
    int len = strlen(text);
    int wordCounter = 0;
    int latterCounter = 0;
    int sentenceCounter = 0;
    int i;
    //cheking to see if the string is empty
    if (len >= 0)
    {
        //looping over all the characters in the string to count word, sentences and latters
        for (i = 0; i <= len - 1; i++)
        {
            //cheking for words
            if (text[i] == ' ')
            {
                //making sure the privius one was not a space as well
                if (i != 0 && text[i - 1] != ' ')
                {
                    wordCounter ++;
                }

            }
            //makeing sure with ascii table the curent chare is a latter and not a simbel
            if (((int)text[i] >= 65 && (int)text[i] <= 90) || ((int)text[i] >= 97 && (int)text[i] <= 122))
            {
                latterCounter ++;
            }
            if (text[i] == '.' || text[i] == '!' || text[i] == '?')
            {
                sentenceCounter ++;
            }

        }
        wordCounter++;
    }
    float avarageLet;
    float avarageSen;
    avarageLet = ((float)latterCounter / (float)wordCounter) * 100;
    avarageSen = ((float)sentenceCounter / (float)wordCounter) * 100;
    int Grade = (int) round((0.0588 * avarageLet) - (0.296 * avarageSen) - 15.8);
    if (Grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (Grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", Grade);
    }
}