#include "lists.h"

/**
  * check_cycle - checks for a cycle in a linked list
  * @list: list
  * Return: 1 if cycle is found, 0 otherwise
  */
int check_cycle(listint_t *list)
{
    listint_t *tortuga = list, *liebre = list;

    if (!list)
        return (0);
    while (tortuga && liebre && liebre->next)
    {
        tortuga = tortuga->next;
        liebre = liebre->next->next;
        if (tortuga == liebre)
            return (1);
    }
    return (0);
}
