// Implements a dictionary's functionality

#include <stdbool.h>

#include "dictionary.h"

#include <stdlib.h>

#include <string.h>

#include <ctype.h>

# include <stdio.h>

#include <strings.h>



int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];
//node *n = malloc(sizeof(node));
//strcpy(n->word, "hellow");
//n->next = NULL;

/* Print all the elements in the linked list */
//void print(node *head) {
//    node *current_node = head;
//   	while ( current_node != NULL) {
//        printf("%d ", current_node->word);
//        current_node = current_node->next;
//    }
//}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int found = 0;
    int hashRes = 0;
    hashRes = hash(word);
    if (table[hashRes] == NULL)
        {
            return false;
        }

     node *t = malloc(sizeof(node));
     t = table[hashRes];
     while(t != NULL)
     {
        if(strcasecmp(t->word, word) == 0)
        {
            t = NULL;
            free(t);
            return true;
        }
        else
        {
            t = t->next;
        }

     }
     //printf("%s", word);
     free(t);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    //printf("%i\n", word[0]);
    if (word[0] >= 97 && word[0] <= 122)
    {
        //printf("lower case\n");
        return(word[0] - 97);
    }
        if (word[0] >= 65 && word[0] <= 90)
    {
        //printf("upper case\n");
        return(word[0] - 65);
    }
    return 0;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    for (int i =0; i<26;i++)
    {
        table[i] = NULL;
    }
    // TODO use fopen() to open the file and check if NULL
    //fscanf(file, "%s", word) until return EOF (end of file)
    //malloc to each word and check if return null and use strcpy to copy the string to the node

    FILE *fp;
    fp=fopen(dictionary, "r");
    if(fp == NULL)
    {
        printf("didnt open the file");
        return 0;
    }
    int hashRes = 0;
    //printf("%p\n",(void *) &fp);
    char temp[46];
    while (fscanf(fp,"%s",temp)==1)
    {
         hashRes = hash(temp);
         //printf("%d <--\n", hashRes);
         node *n = malloc(sizeof(node));
         int x = 0;
            strcpy(n->word, temp);
            for(int foo=0;foo<=strlen(temp);foo++)
            {
            if(temp[foo]>=65&&temp[foo]<=90)
                {
                    temp[foo]=temp[foo]+32;
                }
            }
            strcpy(n->word, temp);

         if(n == NULL)
         {
            table[hashRes] = n;
            n->next = NULL;
            word_count ++;
         }
         else
         {
            n->next = table[hashRes];
            table[hashRes] = n;
            word_count ++;
         }

   }

    //printf("\n%s -> %s -> %s\n", table[1]->word, table[1]->next->word, table[1]->next->next->word);
    fclose(fp);

    return 1;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
   for(int i=0;i<N;i++) // loop thru all the arrays
   {

    node *tmp1=table[i];
    while(tmp1!=NULL)
        {
           node *tmp2 = tmp1;
            tmp1 = tmp1 -> next;
            free(tmp2);
        }
   }
    return true;
}
