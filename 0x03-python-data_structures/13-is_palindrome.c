#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
    int count = 1, i;
    listint_t *run1, *run2, *new, *new2;

    if (!head)
        return(NULL);
    run = *head;
    while(run->next)
    {
        run = run->next;
        count++;
    }
    run2 = *head;
    for(i = 0; i != (count/2); i++)
    {
        run2 = run2->next;
        if(i + 1 == (count/2))
        {
             new = run2;
             new->next = run2->next;
        }
    }
    new2 = *head
    for(x = 0; x != (count/2); x++)
    {
        if(new->n != new2->n)
            return(0);
    }
    return(1);
}
