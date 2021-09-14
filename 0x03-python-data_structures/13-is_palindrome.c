#include "lists.h"
/**
 * is_palindrome - palindrome
 * @head: head
 * Return: int
 */
int is_palindrome(listint_t **head)
{
    listint_t *h = *head;

    int b[1024], i, j;
    
    i = 0;
    j = 0;

    if(*head != NULL)
    {
        while (h)
        {
            b[i] = h->n;
            h = h->next;
            i++;
        }
        while (j < i / 2)
        {
            if(b[j] == b[i - j - 1])
            {
                j++;
            }
            else
            {
                return(0);
            }
        }
    }
    return (1);
}
