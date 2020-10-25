#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int r = 0;
    int g = 0;
    int b = 0;
    long temp = 0.0;
    int avg = 0;
    for(int i = 0;i<height;i++)
    {
        for(int j=0;j<width;j++)
        {
            temp = 0.0;
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            b = image[i][j].rgbtBlue;
            avg = round((r + g + b)/3.0);
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int half = width / 2;
    for(int i = 0; i< height; i++)
    {
        for(int j =0; j< half ;j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_blure[height][width];
    int count = 0;
    int red = 0;
    int green =0 ;
    int blue = 0;
    int now_green = 0;
    int now_blue = 0;
    int now_red = 0;

    for(int i = 0; i < height; i++)
    {
        for(int j=0;j < width ;j++)
        {
            //printf("%i,%i,%i",image[i][j].rgbtRed,image[i][j].rgbtGreen,image[i][j].rgbtBlue);
            now_red = image[i][j].rgbtRed;
            now_green = image[i][j].rgbtGreen;
            now_blue = image[i][j].rgbtBlue;
            for(int k= i-1; k <= i+1; k++ )
            {
                for(int m = j-1; m <= j+1; m++)
                {
                    if(k >= 0 && m >= 0 && k < height && m < width )
                    {
                      red += image[k][m].rgbtRed;
                      green += image[k][m].rgbtGreen;
                      blue += image[k][m].rgbtBlue;
                      count ++;
                    }
                }
            }
            image_blure[i][j].rgbtRed = red / count;
            image_blure[i][j].rgbtGreen = green / count;
            image_blure[i][j].rgbtBlue = blue / count;
            count = 0;
            red= 0 ;
            green = 0;
            blue = 0;
        }
    }

    for(int i = 0; i < height; i++)
    {
        for(int j=0;j < width ;j++)
        {
           image[i][j] = image_blure[i][j];
        }
    }

    return ;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
