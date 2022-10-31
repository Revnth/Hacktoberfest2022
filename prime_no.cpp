#include <iostream>
using namespace std;

int checkPrime(int num)
{
    if(num < 2){
        return 0;
    }
    else{   
       int x = num/2;
        for(int i = 2; i < x; i++)
        {
            if(num % i == 0)
            {
                return 0;
            }
        }
    }
    
    return 1;
}

int main()
{
    int a = 1, b = 100;
    
    for(int i=a; i <= b; i++){
        if(checkPrime(i))
            cout<<i<<" ";
    }
 
    return 0;
}
