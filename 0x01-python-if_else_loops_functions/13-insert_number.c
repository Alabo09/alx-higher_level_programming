#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list
 * @number: Number to store in the new node
 * Return: Pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner, *new;

	runner = *head;

	/* Allocate memory for the new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	/* Set the value of the new node */
	new->n = number;

	/* If the list is empty or the new node is smaller than the first node */
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	/* Traverse the list to find the correct position for the new node */
	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			runner->next = new;
			return (new);
		}
		runner = runner->next;
	}

	/* If the new node is the largest, add it at the end */
	new->next = NULL;
	runner->next = new;
	return (new);
}
