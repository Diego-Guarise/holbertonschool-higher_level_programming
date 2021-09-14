#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * isPalindrome - checkea si es polindrome
 * @left: puntero que apunta al inicio
 * @right: puntero que va hasta el final y vuelve dentro de recursividad
 * Return: 1 si es palindrome, 0 sino lo es
 */
int isPalindrome(listint_t **left, listint_t *right)
{
	int true;

	if (right == NULL)
		return (1);

	if (isPalindrome(left, right->next))
		true = 1;
	else
		true = 0;
	if (!true)
		return (0);
	if (right->n == (*left)->n)
		true = 1;
	else
		true = 0;

	*left = (*left)->next;

	return (true);
}

/**
 * is_palindrome - compara el resultado con ispalindrome
 * @head: lista
 * Return: 1 si es palindrome, 0 sino es
 */
int is_palindrome(listint_t **head)
{
	int check;

	check = isPalindrome(head, *head);
	return (check);
}
