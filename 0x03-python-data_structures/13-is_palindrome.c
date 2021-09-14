#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * isPalindromeUtil - asdasd
 * @left: asdasd
 * @right: asdasd
 * Return: 1 if palindrome, 0 otherwise
 */
int isPalindromeUtil(listint_t **left, listint_t *right)
{
	int true;

	if (right == NULL)
		return (1);

	if (isPalindromeUtil(left, right->next))
		true = 1;
	if (!true)
		return (0);
	if (right->n == (*left)->n)
		true = 1;
	else
		return (0);

	*left = (*left)->next;

	return (true);
}

/**
 * is_palindrome - asdasd
 * @head: asdasd
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int check;

	check = isPalindromeUtil(head, *head);
	return (check);
}
