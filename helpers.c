#include "helpers.h"
#include <math.h>

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
            temp = (r + g + b)/3;
            avg = round(temp);
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
    RGBTRIPLE temp;
    for(int i = 0; i< height; i++)
    {
        for(int j =0; j< round(width/2);j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width-j];
            image[i][width-j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_blure[height][width];
    int count;
    int r=0;
    int g=0;
    int b=0;
    for(int i = 0; i < height; i++)
    {
        for(int j =0; j<width;j++)
        {
            image_blure[i][j].rgbtRed = 0;
            image_blure[i][j].rgbtGreen = 0;
            image_blure[i][j].rgbtBlue = 0;
        }
    }
    for(int i = 0; i < height; i++)
    {
        for(int j =0; j<width;j++)
        {
            image[i][j].rgbtRed  = image_blure[i][j].rgbtRed;
            image[i][j].rgbtGreen = image_blure[i][j].rgbtGreen;
            image[i][j].rgbtBlue = image_blure[i][j].rgbtBlue;
        }
    }
    return ;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
