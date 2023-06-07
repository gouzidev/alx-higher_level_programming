#include "lists.h"
/**
 * check_cycle - checks cycle
 * @list: pointer to int node list
 *
 * Return: integer indicating if cycle or not
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;
if (!list)
{
return (0);
}
while (fast && fast->next && slow)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
{
return (1);
}
}
return (0);
}
