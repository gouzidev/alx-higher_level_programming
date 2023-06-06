#include "lists.h"

/**
 * insert_node - prints all elements of a listint_t list
 * @head: pointer to head of list
 * @number: pointer to head of list
 * Return: number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *prev;
listint_t *curr;
int found = 0;

new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}
new_node->n = number;
new_node->next = NULL;
if (*head == NULL)
{
*head = new_node;
return (new_node);
}
prev = *head;
curr = *head;
if (number < (*head)->n)
{
new_node->next = curr;
*head = new_node;
return (new_node);
}

while (curr)
{
if (number < curr->n && !found)
{
prev->next = new_node;
new_node->next = curr;
found = 1;
}
prev = curr;
curr = curr->next;
}
if (!found)
prev->next = new_node;
return (new_node);
}
