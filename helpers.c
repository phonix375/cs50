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
    float count = 0;
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
            image_blure[i][j].rgbtRed = round(red / count);
            image_blure[i][j].rgbtGreen = round(green / count);
            image_blure[i][j].rgbtBlue = round(blue / count);
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
    RGBTRIPLE image_edge[height][width];

    for(int i = 0; i < height; i++)
    {
        for(int j=0;j < width ;j++)
        {
           image_edge[i][j] = image[i][j];
        }
    }

  for(int i = 0; i < height; i++)
    {
        for(int j=0;j < width ;j++)
        {
            float gx_r = 0.0;
            float gx_g = 0.0;
            float gx_b = 0.0;

            float gy_r = 0.0;
            float gy_g = 0.0;
            float gy_b = 0.0;
            int GX[9] = {-1,0,1,-2,0,2,-1,0,1};
            int GY[9] = {-1,-2,-1,0,0,0,1,2,1};
            float temp = 0.0;


            int count = 0;
            for(int k= i-1; k <= i+1; k++ )
            {


                for(int m = j-1; m <= j+1; m++)
                {

                    if(k >= 0 && m >= 0 && k < height && m < width )
                    {
                      gx_r +=  GX[count] * image_edge[k][j].rgbtRed;
                      gx_g +=  GX[count] * image_edge[k][j].rgbtGreen;
                      gx_b +=  GX[count] * image_edge[k][j].rgbtBlue;

                      gy_r += GY[count] * image_edge[k][j].rgbtRed;
                      gy_g += GY[count] * image_edge[k][j].rgbtGreen;
                      gy_b += GY[count] * image_edge[k][j].rgbtBlue;
                    }
                    count++;
                }
            }
            if(sqrt((gx_r * gx_r) +  (gy_r * gy_r)) > 255)
            {
               image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = round(sqrt((gx_r * gx_r +  gy_r * gy_r)));
            }
            if(round(sqrt(gx_g * gx_g + gy_g * gy_g) > 255))
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = round(sqrt(gx_g * gx_g + gy_g * gy_g ));
            }
            if(round(sqrt((gx_b * gx_b) +  (gy_b * gy_b))) > 255)
            {
               image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = round(sqrt((gx_b * gx_b) +  (gy_b * gy_b)));
            }
        }
    }


    return;
}