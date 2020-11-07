#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("please provide only one argument\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    int ImageNumber = 0;
    uint8_t buffer[512];
    FILE *outputFile = NULL;
    int found_image = 0;

    while (fread(&buffer, sizeof(char), 512, file))  // going over the file
    {

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) // chacking the first 4 bites
        {
            printf("%x %x %x\n", buffer[0], buffer[1], buffer[2]);
            if (found_image == 1) //if image found alrady
            {
                fclose(outputFile);
            }
            else
            {
                found_image = 1;
            }
            char filename[8];
            sprintf(filename, "%03i.jpg", ImageNumber);
            outputFile = fopen(filename, "w");
            ImageNumber++;
        }
        if (found_image == 1)//once new JPEGS are found
        {
            fwrite(&buffer, 512, 1, outputFile);
        }
    }


    //printf("%i");
    fclose(file);
    return 0;

}
