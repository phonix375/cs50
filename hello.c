#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //this asks for the usert name
    string name = get_string("What is your name?\n");
    //this is printing to the screen Hello and the user name
    printf("hello, %s\n", name);
}