#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *run, *prev;

    if (!head)
        return(NULL);
    
    new = malloc(sizeof(listint_t));
    if (!new)
        return(NULL);
    run = *head;
    new->n = number;
    while (run && run->next && number > run->n)
    {
        prev = run;
        run = run->next;
    }
    if (prev)
        prev->next = new;
    new->next = run;
    return(new);
}
