#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = NULL, *run, *prev;

    if (!head)
        return(NULL);
    
    new = malloc(sizeof(listint_t));
    if (!new)
        return(NULL);
    run = *head;
    while (run && number > run->n)
    {
        prev = run;
        run = run->next;
        if (run->n < )
    }
}
