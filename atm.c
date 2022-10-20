#include <stdio.h>
#include <stdlib.h>

int main () {
    int pin=1234, enteredPin, opt, amt=1, cnt=0, continueTransaction=1;
    float bal = 10000;

    printf("\n\t\t\t= = = = = = = = = = = = = = = = = = = = *Welcome to ATM* = = = = = = = = = = = = = = = = = = = =");

    while (pin != enteredPin) {
        printf("\nPlease enter your PIN : ");
        scanf("%d", &enteredPin);
        if (enteredPin != pin) {
            printf("Invalid Pin !!!\n");
            cnt++;
        }
        if (cnt == 3 && enteredPin != pin) {
            exit(0);        }
    }

    while (continueTransaction != 0) {
        printf("\n\t\t\t\t\t\t==========*Available Transactions*==========");
        printf("\n\n\t\t1.Withdraw");
        printf("\n\t\t2.Deposit");
        printf("\n\t\t3.Check Balance");
        printf("\n\n\t\tPlease select the option : ");
        scanf("%d", &opt);

        switch (opt) {
            case 1: 
                while (amt%500 != 0) {
                    printf("\n\t\tEnter the amount : ");
                    scanf("%d", &amt);
                    if (amt%500 != 0) {
                        printf("\n\t\t\t\t\t\tThe amount should be multiple of 500\n");
                    }
                }
                if (bal < amt) {
                    printf("\n\t\t\t\t\t\tInsufficient Balance\n");
                    amt = 1;
                    break;
                }
                else {
                    bal = bal - amt;
                    printf("\n\t\t\t\t\tYou have withdrawn Rs.%d. Your new balance is Rs.%.2f\n", amt, bal);
                    amt = 1;
                    break;
                }
            case 2:    
                printf("\n\t\t\t Please enter the amount : ");
                scanf("%d", &amt);
                bal = bal + amt;
                printf("\n\t\t\t\t\tYou have deposited Rs.%d. Your new balance is Rs.%.2f\n", amt, bal);
                amt = 1;
                break;
            case 3: 
                printf("\n\t\t\t\t\t\tYour current balance is Rs.%.2f\n", bal);
                break;
            default:
                printf("\n\t\t\t\t\t\tInvalid Option !!!\n");    
        }
        printf("\n\t\tDo you wish to perform another transaction?\n\t\tPress 1 for YES\n\t\tPress 0 for NO\n\t\t");
        scanf("%d", &continueTransaction);
    }
    printf("\n\t\t\t= = = = = = = = = = = = = = = = = *Thank you for using the ATM* = = = = = = = = = = = = = = = = =");
    printf("\n\t\t\t\t\t\t\t\tHave a Good Day\n");
}