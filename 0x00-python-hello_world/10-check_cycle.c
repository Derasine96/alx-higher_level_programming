#include "lists.h"
/**
 * check_cycle - check for circular linked list
 * @list: address of the head node
 * Return: 0 if no circle, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *temp;

	if (list == NULL)
		return (0);

	ptr = list;
	temp = list->next;

	while (ptr && temp && temp->next)
	{
		if (ptr == temp)
			return (1);
		ptr = ptr->next;
		temp = temp->next->next;
	}
	return (0);
}
