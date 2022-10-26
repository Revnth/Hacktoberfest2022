#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int i = 0, j = 0;

struct InfixToPostfix
{
    int size;
    int top;
    char *arr;
};

int isEmpty(struct InfixToPostfix *ptr)
{
    if (ptr->top == (-1))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isFull(struct InfixToPostfix *ptr)
{
    if (ptr->top == (ptr->size - 1))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void push(struct InfixToPostfix *ptr, char data)
{
    if (isFull(ptr))
    {
        printf("stack overflow.");
    }
    else
    {
        ptr->arr[ptr->top + 1] = data;
        ptr->top++;
    }
}

int pop(struct InfixToPostfix *ptr)
{
    if (isEmpty(ptr))
    {
        printf("stack underflow.\n");
        return -1;
    }
    else
    {
        int val = (ptr->arr[ptr->top]);
        ptr->top--;
        return val;
    }
}

int isOperater(char a)
{
    if (a == '*' || a == '/' || a == '-' || a == '+')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int precedence(char a)
{
    if (a == '+' || a == '-')
    {
        return 1;
    }
    if (a == '/' || a == '*')
    {
        return 2;
    }
    else
    {
        return 0;
    }
}

int main(int argc, char const *argv[])
{
    char infix[10], postfix[10];
    struct InfixToPostfix *sp;
    printf("\nHi.\n");
    sp->size = 10;
    sp->top = -1;
    sp->arr = (char *)malloc(sizeof(char) * (sp->size));
    printf("\nEnter an inFix expression-> ");
    scanf("%s", &infix);

    printf("\nThe entered infix expression is -> %s\n", infix);

    while (infix[i] != '\0')
    {
        if (!isOperater(infix[i]))
        {
            postfix[j] = infix[i];
            i++;
            j++;
        }
        else
        {
            if (precedence(infix[i]) > precedence(sp->arr[sp->top]))
            {
                push(sp, infix[i]);
                i++;
            }
            else
            {
                postfix[j] = pop(sp);
                j++;
                i++;
            }
        }
    }
    while (!isEmpty(sp))
    {
        postfix[j] = pop(sp);
        j++;
    }
    postfix[j] = '\0';

    printf("\nThe converted postfix expression is -> %s", postfix);
    return 0;
}
