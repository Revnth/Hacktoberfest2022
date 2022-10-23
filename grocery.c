#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *productName[] = {"All Out", "Coconut oil", "Kesar", "Detergent", "sugar", "maida", "Vegetable oil", "Face cream", "hair oil", "salt", "toffee", "bhujiya", "Muesli", "CornFlakes", "Oats", "milk powder", "turmeric powder", "hair shampoo", "ghee", "Deoderant"};
char product_name[19][20];
int product_quantity[19];
int count1 = 0, total_bill = 0, total_bill1 = 0, discount;
int allout_p = 25, coconut_oil_p = 25, kesar_p = 100, Detergent_p= 100, sugar_p = 20, maida_p = 100, vegetable_oil_p = 200, face_cream_p = 40, hair_oil_p = 120, salt_p = 50, toffee_p = 40, bhujiya_p = 45, muesli_p = 200, cornflakes_p = 100, oats_p = 100, milk_powder_p = 150, turnmeric_powder_p = 200, hair_shampoo_p=350, ghee_p = 300, deoderant_p = 70;
void generate_bill()
{
    printf("\n\t    **** GROCERY STORE BILL ****\n");
    printf("|--------------------------------------------------------|\n");
    printf("|  Product\t\tQuantity\t\tPrice                          |\n");
    printf("|--------------------------------------------------------|\n");
    for (int i = 0; i < count1; i++)
    {
        if (!strcmp("All Out", product_name[i]))
        {
            printf("|  %s           \t%dkg     \t\t%d  |\n", product_name[i], product_quantity[i], allout_p*product_quantity[i]);
            printf("|--------------------------------------------------------|\n");
        }
        else if (!strcmp("Coconut oil", product_name[i]))
        {
            printf("|  %s            \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], coconut_oil_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("Kesar", product_name[i]))
        {
            printf("|  %s     \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], kesar_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("Detergent", product_name[i]))
        {
            printf("|  %s      \t%dkg     \t\t%d  \n", product_name[i], product_quantity[i], Detergent_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("sugar", product_name[i]))
        {
            printf("|  %s            \t%dkg     \t\t%d  \n", product_name[i], product_quantity[i], sugar_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("maida", product_name[i]))
        {
            printf("|  %s            \t%dkg    \t\t%d  \n", product_name[i], product_quantity[i], maida_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("Vegetable oil", product_name[i]))
        {
            printf("|  %s                 \t%dltr      \t\t%d  \n", product_name[i], product_quantity[i], vegetable_oil_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("Face cream", product_name[i]))
        {
            printf("|  %s          \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], face_cream_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("hair oil", product_name[i]))
        {
            printf("|  %s    \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], hair_oil_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("salt", product_name[i]))
        {
            printf("|  %s       \t%dkg     \t\t%d  \n", product_name[i], product_quantity[i], salt_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("toffee", product_name[i]))
        {
            printf("|  %s           \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], toffee_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("bhujiya", product_name[i]))
        {
            printf("|  %s                \t%dkg     \t\t%d  \n", product_name[i], product_quantity[i], bhujiya_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("Muesli", product_name[i]))
        {
            printf("|  %s          \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], muesli_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("CornFlakes", product_name[i]))
        {
            printf("|  %s             \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], cornflakes_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("Oats", product_name[i]))
        {
            printf("|  %s               \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], oats_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("milk powder", product_name[i]))
        {
            printf("|  %s          \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], milk_powder_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("turmeric powder", product_name[i]))
        {
            printf("|  %s      \t%dkg     \t\t%d  \n", product_name[i], product_quantity[i], turnmeric_powder_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("hair shampoo", product_name[i]))
        {
            printf("|  %s            \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], hair_shampoo_p*product_quantity[i]);
            printf("|--------------------------------------------------------\n");
        }
        else if (!strcmp("ghee", product_name[i]))
        {
            printf("|  %s               \t%dkg     \t\t%d  \n", product_name[i], product_quantity[i], ghee_p*product_quantity[i]);
            printf("|-------------------------------------------------------\n");
        }
        else if (!strcmp("Deoderant", product_name[i]))
        {
            printf("|  %s          \t%dpac      \t\t%d  \n", product_name[i], product_quantity[i], deoderant_p*product_quantity[i]);
            printf("|-------------------------------------------------------\n");
        }
    }
    printf("| Total product %d \t\tTotal amount    %d\n", count1, total_bill1);
    printf("|--------------------------------------------------------\n");
    printf("|                  \t\tDiscount        %d\n", discount);
    printf("|--------------------------------------------------------\n");
    printf("|                  \t\tPayable ammount %d\n", total_bill);
    printf("|--------------------------------------------------------\n");
}
void calculate_bill()
{
    char choose;
    for (int i = 0; i < count1; i++)
    {
        if (!strcmp("All Out", product_name[i]))
        {
            total_bill += allout_p * product_quantity[i];
        }
        else if (!strcmp("Coconut oil", product_name[i]))
        {
            total_bill += coconut_oil_p* product_quantity[i];
        }
        else if (!strcmp("Kesar", product_name[i]))
        {
            total_bill += kesar_p * product_quantity[i];
        }
        else if (!strcmp("Detergent", product_name[i]))
        {
            total_bill += Detergent_p * product_quantity[i];
        }
        else if (!strcmp("sugar", product_name[i]))
        {
            total_bill += sugar_p * product_quantity[i];
        }
        else if (!strcmp("maida", product_name[i]))
        {
            total_bill += maida_p * product_quantity[i];
        }
        else if (!strcmp("Vegetable oil", product_name[i]))
        {
            total_bill += vegetable_oil_p * product_quantity[i];
        }
        else if (!strcmp("Face cream", product_name[i]))
        {
            total_bill += face_cream_p * product_quantity[i];
        }
        else if (!strcmp("hair oil", product_name[i]))
        {
            total_bill += hair_oil_p * product_quantity[i];
        }
        else if (!strcmp("salt", product_name[i]))
        {
            total_bill += salt_p * product_quantity[i];
        }
        else if (!strcmp("toffee", product_name[i]))
        {
            total_bill += toffee_p * product_quantity[i];
        }
        else if (!strcmp("bhujiya", product_name[i]))
        {
            total_bill += bhujiya_p * product_quantity[i];
        }
        else if (!strcmp("Muesli", product_name[i]))
        {
            total_bill += muesli_p * product_quantity[i];
        }
        else if (!strcmp("CornFlakes", product_name[i]))
        {
            total_bill += cornflakes_p * product_quantity[i];
        }
        else if (!strcmp("Oats", product_name[i]))
        {
            total_bill += oats_p * product_quantity[i];
        }
        else if (!strcmp("milk powder", product_name[i]))
        {
            total_bill += milk_powder_p * product_quantity[i];
        }
        else if (!strcmp("turmeric powder", product_name[i]))
        {
            total_bill += turnmeric_powder_p * product_quantity[i];
        }
        else if (!strcmp("hair shampoo", product_name[i]))
        {
            total_bill += hair_shampoo_p * product_quantity[i];
        }
        else if (!strcmp("ghee", product_name[i]))
        {
            total_bill += ghee_p * product_quantity[i];
        }
        else if (!strcmp("Deoderant", product_name[i]))
        {
            total_bill += deoderant_p * product_quantity[i];
        }
    }
    total_bill1 = total_bill;
    if (total_bill >= 15000)
    {
        discount = (15 * total_bill) / 100;
        total_bill = total_bill - discount;
    }
    else if (total_bill >= 10000 && total_bill < 15000)
    {
        discount = (10 * total_bill) / 100;
        total_bill = total_bill - discount;
    }
    else if (total_bill >= 5000 && total_bill < 10000)
    {
        discount = (5 * total_bill) / 100;
        total_bill = total_bill - discount;
    }
repeate:
    printf("\nIf you want to generate your bill then press 'Y' otherwise 'N': ");
    fflush(stdin);
    scanf("%c", &choose);
    if (choose == 'Y' || choose == 'y')
    {
        generate_bill();
    }
    else if (choose == 'N' || choose == 'n')
    {
        exit(0);
    }
    else
    {
        printf("Invalid character tyr again\n");
        goto repeate;
    }
}
void main()
{
    char ch, temp_str[20];
    int check,count=0;
    printf("\n\n   *** GROCERY STORE***\n\n");
    printf("   Here are our store discount rates\n");
    printf("***************************************\n");
    printf("| less than Rs.5000 buy 0%% discount      |\n");
    printf("|-------------------------------------|\n");
    printf("| greater than Rs.5000 buy 5%% discount   |\n");
    printf("|-------------------------------------|\n");
    printf("| greater than Rs.10000 buy 10%% discount |\n");
    printf("|-------------------------------------|\n");
    printf("| greater than Rs.15000 buy 15%% discount |\n");
    printf("***************************************\n\n");
    printf("Please enter all product bought by you\n");
    for (int i = 0; i < 20; i++)
    {

    repeate1:
        count=0;
        printf("Enter product name : ");
        fflush(stdin);
        gets(temp_str);
        for (int j = 0; j < 20; j++)
        {
            check = strcmp(temp_str, productName[j]);
            if (check == 0)
            {
                strcpy(product_name[count1], temp_str);
            }
            else
            {
                count++;
                if (count == 20)
                {
                    printf("Invalid product name\n");
                    goto repeate1;
                }
            }
        }
    repeate2:
        printf("Enter quantity : ");
        scanf("%d", &product_quantity[count1]);
        if (product_quantity[count1] < 1)
        {
            printf("Invalid quantity try again\n");
            goto repeate2;
        }
        count1++;
    repeate:
        printf("If you have entered all product then Press 'Y' otherwise 'N' :");
        fflush(stdin);
        scanf("%c", &ch);
        if (ch == 'Y' || ch == 'y')
        {
            calculate_bill();
            exit(0);
        }else if (ch=='N'||ch=='n')
        {
            printf("");
        }        
        else
        {
            printf("Invalid press try again\n");
            goto repeate;
        }
    }
    printf("\nWe have only 20 product\n\n");
    calculate_bill();
}