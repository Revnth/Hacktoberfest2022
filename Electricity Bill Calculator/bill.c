#include<stdlib.h>
#include<stdio.h>

#define watt 1000
#define time 24
#define  cost 6.15

int main()
{

    int day;
    char ch;
    float kwh,unit,bill;
    printf("\n\n****Electricity Bill Calculator****\n\n");
    do
    {   
    printf("\nEnter no of days:");
    scanf("%d",&day);
    
    kwh = (float)watt*time*day;
    unit = kwh/(float)watt;
    
    bill = unit * cost;
    
    printf("Total units consumed by the user:%.4f",unit);
    printf("\nThe cost of per unit electricity:%.4f",cost);
    printf("\nTotal bill of electricity for %d days is: Rs%.4f",day,bill);

    printf("\n\nCaculate another bill?[y/n]:");
    scanf("%c%c",&ch,&ch);
    }while(ch=='y' || ch=='Y');
}
