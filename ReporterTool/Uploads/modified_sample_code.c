#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
 char b = 0;
 
void main()
{
    struct node
    {
        int num;
        struct node *ptr;
    };
    typedef struct node NODE;
 
    NODE *head, *first, *temp = 0;
    int count = 0;
    int choice = 1;
    first = 0;
	
	
    while (choice)
    {
        head  = (NODE *)malloc(sizeof(NODE));
        printf("Enter the data item\n");
        scanf("%d", head-> num);
        if (first != 0)
        {
            temp->ptr = head;
            temp = head;
        }
        else
        {
            first = temp = head;
        }
        fflush(stdin);
        printf("Do you want to continue(Type 0 or 1)?\n");
        scanf("%d", &choice);
		/*choice = 1;*/ 		/*Modified for Polyspace_Red*/
 
    }
    temp->ptr = 0; /* Red Error ID 21 */
    /*  reset temp to the beginning */
    temp = first;
    printf("\n status of the linked list is\n");
    while (temp != 0)
    {
        printf("%d=>", temp->num);
        count++;
        temp = temp -> ptr;
    }
    printf("NULL\n");
    printf("No. of nodes in the list = %d\n", count);
}

void entry_point(void)
{
	int a = 1; /* Red Error ID 11 */
	
	printf("%d\n", a);
	
}

void entry_point_1(void)
{
	int arr[10] = {0,0,0,0,0,0,0,0,0,0}; /* Red Error ID 13 */
	
	printf("%d\n", arr[9]);
}

void entry_point_2(void)
{
	//char a = (char)((0xFFFFFFFFFF) & 0xff); /* Red Error ID 16 */
	
}

void entry_point_3(void)
{
	int a = b;
}

