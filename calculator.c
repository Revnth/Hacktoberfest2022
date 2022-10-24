#include <stdio.h>  
int main()  
{   
    char opt,ch;  
    int n1, n2;   
    float res;  
    do
    {
    printf (" Choose an operator(+, -, *, /) to perform the operation in C Calculator \n ");  
    scanf ("%c%c",&opt, &opt); 
    if (opt == '/' )  
    {  
        printf (" You have selected: Division");  
    }  
    else if (opt == '*')  
    {  
        printf (" You have selected: Multiplication");  
     }  
       
    else if (opt == '-')  
    {  
        printf (" You have selected: Subtraction");  
     }  
        else if (opt == '+')  
    {  
        printf (" You have selected: Addition");  
     }     
    printf (" \n Enter the first number: ");  
    scanf(" %d", &n1);   
    printf (" Enter the second number: ");  
    scanf (" %d", &n2);  
      
    switch(opt)  
    {  
        case '+':  
            res = n1 + n2;  
            printf (" Addition of %d and %d is: %.2f", n1, n2, res);  
            break;  
          
        case '-':  
            res = n1 - n2;  
            printf (" Subtraction of %d and %d is: %.2f", n1, n2, res);  
            break;  
              
        case '*':  
            res = n1 * n2;  
            printf (" Multiplication of %d and %d is: %.2f", n1, n2, res);  
            break;            
          
        case '/':  
            if (n2 == 0)   
            {  
                printf (" \n Divisor cannot be zero. Please enter another value ");  
                scanf ("%d", &n2);        
                }  
            res = n1 / n2;
            printf (" Division of %d and %d is: %.2f", n1, n2, res);  
            break;  
        default:   
            printf (" Something is wrong!! Please check the options ");               
    }
    printf("\nDo want use again?(y/n)");
    scanf("%c%c",&ch,&ch);
    }while(ch=='y'||ch=='Y');
    return 0;  
}  
