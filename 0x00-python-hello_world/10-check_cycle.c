#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *last;

	if (list == NULL || list->next == NULL)
		return (0);

	first = list->next;
	last = list->next->next;

	while (first && last && last->next)
	{
		if (first == last)
			return (1);

		first = first->next;
		last = last->next->next;
	}

	return (0);
}
