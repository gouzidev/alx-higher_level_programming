#include "lists.h"

/**
 * comp_linked_lists - prints all elements of a listint_t list
 * @h1: pointer to head of list
 * @h2: pointer to head of list
 * Return: 1 if pal else 0
 */

int comp_linked_lists(listint_t *h1, listint_t *h2)
{
while (h1 && h2)
{
if (h1->n != h2->n)
{
return (0);
}
h1 = h1->next;
h2 = h2->next;
}
return (1);
}


/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to pointer to head of list
 * Return: 1 if pal else 0
 */
int is_palindrome(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *next = NULL;
    listint_t *curr = *head;
    listint_t *fast = *head;
    int palindrome_comp = 0;

    if (head == NULL || *head == NULL)
        return (1);
    if ((*head)->n && (*head)->next == NULL)
        return 1;

    while (fast)
    {
        fast = fast->next;
        if (fast)
        {
            fast = fast->next;
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        else
            curr = curr->next;
    }

    palindrome_comp = comp_linked_lists(prev, curr);

    return (palindrome_comp);

}
