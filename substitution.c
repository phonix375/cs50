#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
     string plantext;
    if(argc < 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    int keylen = strlen(argv[1]);
    if (keylen != 26)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }


    plantext = get_string("plaintext: ");
    char ciphertext[(int)strlen(plantext)];

    for (int i=0;i < strlen(plantext); i++)
    {
        if(isalpha(plantext[i]))
        {
            //check if upper case
            if((int)plantext[i] >=  65 && (int)plantext[i] <= 90)
            {
                printf("i need apper %c ",argv[1][(int)plantext[i]-65]);
                if(isupper(argv[1][(int)plantext[i]-65]))
                {
                   ciphertext[i] = argv[1][(int)plantext[i]-65];
                }
                else
                {
                    ciphertext[i] = (char)((int)argv[1][(int)plantext[i]-65])-32;
                }


            }
            //if plan text lower case
            else
            {
                printf("i need lower %c ",argv[1][(int)plantext[i]-97]);
                if(isupper(argv[1][(int)plantext[i]-97]))
                {
                   ciphertext[i] = (char)((int)argv[1][(int)plantext[i]-97] + 32);
                }
                else
                {
                    ciphertext[i] = (char)((int)argv[1][(int)plantext[i]-97]);
                }


            }

        }
        else
        {
            ciphertext[i] = plantext[i];
        }


    }
    printf("ciphertext: \n");
    for(int j = 0; j < strlen(plantext);j++)
    {
        printf("%c",ciphertext[j]);
    }
    printf("\n");
}
