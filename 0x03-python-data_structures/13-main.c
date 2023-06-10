#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 5);
    add_nodeint_end(&head, 1);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}


// has to run 5 times for 10 ls (even)
// has to run 5 times for 9 ls (odd)
//    + prev = prev->next














    // printf(" curr ") ; printn(curr->n);
    // printf(" curr->next ") ; printn(curr->next->n);
    // printf(" curr->next->next ") ; printn(curr->next->next->n);
    
    // printf(" next ") ; printn(next->n);
    // printf(" next->next ") ; printn(next->next->n);
    // printf(" prev ") ; printn(prev->n);
    // printf(" prev->next ") ; printn(prev->next->n);
    // printf(" prev->next->next ") ; printn(prev->next->next->n);
    // printf("\n");
    // printf("\n");
