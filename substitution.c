#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    string plantext;
    //makeing sure there is at list 2  arguments passed
    if (argc < 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    //cheking the lenght of the key argument
    int keylen = strlen(argv[1]);
    if (keylen != 26)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    //cheking if all carecters are letters
    for (int x = 0; x < keylen; x ++)
    {
        if (!(isalpha(argv[1][x])))
        {
            printf("your key needs to contain just letters\n");
            return 1;
        }
    }
    //cheking for duplicates in the key
    for (int y = 0; y < keylen ; y ++)
    {
        for (int z = 0; z < keylen; z++)
        {
            if (!(y == z))
            {
                if (argv[1][y] == argv[1][z])
                {
                    printf("all carecters maust be unik in the key\n");
                    return 1;
                }
            }
        }
    }



    //asking the user for input
    plantext = get_string("plaintext: ");
    //createing a return string with the size on the input
    char ciphertext[(int)strlen(plantext)];
//compering to key
    for (int i = 0; i < strlen(plantext); i++)
    {
        if (isalpha(plantext[i]))
        {
            //check if upper case
            if ((int)plantext[i] >=  65 && (int)plantext[i] <= 90)
            {
                if (isupper(argv[1][(int)plantext[i] - 65]))
                {
                    ciphertext[i] = argv[1][(int)plantext[i] - 65];
                }
                else
                {
                    ciphertext[i] = (char)((int)argv[1][(int)plantext[i] - 65]) - 32;
                }


            }
            //if plan text lower case
            else
            {
                if (isupper(argv[1][(int)plantext[i] - 97]))
                {
                    ciphertext[i] = (char)((int)argv[1][(int)plantext[i] - 97] + 32);
                }
                else
                {
                    ciphertext[i] = (char)((int)argv[1][(int)plantext[i] - 97]);
                }


            }

        }
        else
        {
            ciphertext[i] = plantext[i];
        }


    }
    //printing the ciphertext by looping
    printf("ciphertext: \n");
    for (int j = 0; j < strlen(plantext); j++)
    {
        printf("%c", ciphertext[j]);
    }
    printf("\n");
}
