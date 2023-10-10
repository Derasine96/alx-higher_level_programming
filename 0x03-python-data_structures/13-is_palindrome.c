#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the first node
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *prev, *half;
	listint_t *current = head;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	fast = head;
	slow = head;
	prev = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	half = slow;
	prev->next = NULL;
}
