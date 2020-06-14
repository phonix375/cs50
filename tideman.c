#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }
    //clear the preferences table
    for(int i = 0; i<candidate_count; i++)
    {
        for(int j = 0; j < candidate_count; j++)
        {
            preferences[i][j] = 0;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];
        for(int f = 0; f < candidate_count; f ++ )
        {
           ranks[f] = 99999;
        }

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }
    for(int i = 0; i < candidate_count; i++)
    {
        for(int j = 0 ; j < candidate_count;j++)
        {
            //printf("| %i |",preferences[i][j]);
        }
       //printf("\n");
    }

    add_pairs();
    for(int i = 0; i<pair_count;i++)
    {
       //printf("prir %i winner %i loser %i\n", i,pairs[i].winner,pairs[i].loser );
    }
     for(int i = 0; i< pair_count; i++)
    {
        //printf("pair %i diffrense %i  between %i - %i\n| ", i,preferences[pairs[i].winner][pairs[i].loser] - preferences[pairs[i].loser][pairs[i].winner], pairs[i].winner,pairs[i].loser );
    }
    sort_pairs();
    //printf("-----------------------------after sort-------------------\n");
    for(int i = 0; i< pair_count; i++)
    {
        //printf("pair %i diffrense %i  between %i - %i\n| ", i,preferences[pairs[i].winner][pairs[i].loser] - preferences[pairs[i].loser][pairs[i].winner], pairs[i].winner,pairs[i].loser );
    }
    //printf("\n");
        for(int i = 0; i<pair_count;i++)
    {
        //printf("prir %i winner %i loser %i\n", i,pairs[i].winner,pairs[i].loser );
    }
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i< candidate_count; i++)
    {
        if(strcmp(candidates[i], name) == 0)
        {
            //printf("found him \n");
            for (int x = 0 ; x < candidate_count; x++)
            {
                if(ranks[x] == i )
                {
                    return false;
                }
            }
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for(int i = 0 ; i < candidate_count; i++)
    {
        for(int j = i+1; j < candidate_count ; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for(int i = 0; i<candidate_count ; i++)
    {
        for(int j = 0; j< candidate_count ; j++)
        {
            if(preferences[i][j] < preferences[j][i])
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int max_index=0;
    pair temp;
    for (int i=0; i< pair_count; i++)
    {
        max_index = i;
        for(int j = i+1 ; j < pair_count;j++)
        {

            if (preferences[pairs[i].winner][pairs[i].loser] - preferences[pairs[i].loser][pairs[i].winner]  < preferences[pairs[j].winner][pairs[j].loser] - preferences[pairs[j].loser][pairs[j].winner])
            {
                max_index = j;
            }
        }
        if(max_index != i)
        {
            //temp = list[i];
            temp.winner = pairs[i].winner;
            temp.loser = pairs[i].loser;
            //list[i] = list[max_index];
            pairs[i].winner = pairs[max_index].winner;
            pairs[i].loser = pairs[max_index].loser;
            //list[max_index] = temp;
            pairs[max_index].winner = temp.winner;
            pairs[max_index].loser = temp.loser;
        }
    }

    return;
}
// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{

    int true_count = 0;
    for(int i= 0; i < pair_count; i++)
    {
        true_count = 0;
        locked[pairs[i].winner][pairs[i].loser] = true;
        for(int x = 0; x < pair_count; x++ )
        {
            for(int y =0;y<pair_count;y++)
            {
                if(locked[y][x] == 1)
                {
                  true_count++;
                  y=pair_count;
                }
            }
        }
        if(true_count == pair_count)
        {
            locked[pairs[pair_count-1].winner][pairs[pair_count-1].loser]= false;
        }
    }
    for(int i = 0; i < pair_count; i++)
    {
        for(int j=0;j<pair_count;j++)
        {
            //printf("| %i |",locked[i][j]);
        }
        //printf("\n");
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    int true_count;
    for(int i=0; i<candidate_count;i++ )
    {
        true_count = 0;
        for(int j = 0; j<candidate_count; j++)
        {
            if(locked[j][i] == 1)
            {
                true_count++;
            }
        }
        if(true_count == 0 )
        {
            printf("%s \n",candidates[i]);
        }
    }
    return;
}

