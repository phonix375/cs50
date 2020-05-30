#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
int main(void)
{
    string text = get_string("TEXT: ");
    int len = strlen(text);
    int wordCounter = 0;
    int latterCounter =0;
    int sentenceCounter =1;
    int i;
    if(len >= 0)
    {
            for (i= 0; i<len-1;i++ )
        {
            if(text[i]==' ')
            {
                if (i != 0 && text[i-1] != ' ')
                {
                    wordCounter ++;
                }

            }
            if( ((int)text[i] >= 65 && (int)text[i] <= 90) || ((int)text[i] >= 97 && (int)text[i] <= 122) )
            {
               latterCounter ++;
            }
            if (  text[i] == '.' || text[i] == '!' || text[i] == '?')
            {
                sentenceCounter ++;
            }

        }
        wordCounter++;
    }
    float avarageLet;
    float avarageSen;
    avarageLet = ((float)latterCounter / (float)wordCounter)*100;
    avarageSen = ((float)sentenceCounter / (float)wordCounter) * 100;
    int Grade =  (int) round((0.0588*avarageLet) - (0.296 * avarageSen) -15.8);
    if(Grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if(Grade < 1 )
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", Grade);
    }

}