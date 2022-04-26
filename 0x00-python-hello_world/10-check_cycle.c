#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *car1 = list;
	listint_t *car2 = list;

	if (!list)
		return (0);

	while (car1 && car2 && car2->next)
	{
		car1 = car1->next;
		car2 = car2->next->next;
		if (car1 == car2)
			return (1);
	}

	return (0);
}
