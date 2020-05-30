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

    for (int i=0;i < keylen; i++)
    {
        if (isalpha(plantext[i]))
        {
            if(islower(plantext[i]))
            {
                ciphertext[i] = argv[1][(int)plantext[i] - 97];
                //convert to lower
            }
            else if(isupper(plantext[i]))
            {
                ciphertext[i] = argv[1][(int)plantext[i] - 65];
                //convert to upper
            }
            else
            {
                 ciphertext[i] = argv[1][i];
            }
        }
    }
    printf("ciphertext: ");
    for(int j = 0; j < strlen(plantext)-1; j++)
    {
        printf("%c",ciphertext[j]);
    }
}