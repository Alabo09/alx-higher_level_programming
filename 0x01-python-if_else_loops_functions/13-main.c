#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - Entry point of the program
 *
 * This program demonstrates the usage of the insert_node function.
 * It creates a sorted linked list, inserts a new node, and prints the result.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;

	/* Adding nodes to the end of the list */
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 402);
	add_nodeint_end(&head, 1024);

	/* Print the original list */
	printf("Original List:\n");
	print_listint(head);
	printf("-----------------\n");

	/* Insert a new node with the value 27 */
	insert_node(&head, 27);

	/* Print the updated list */
	printf("Updated List after Insertion:\n");
	print_listint(head);

	/* Free the allocated memory for the list */
	free_listint(head);

	return (0);
}
}
