#include <iostream>
using namespace std;
int main()
{
int i, j, num;
cin >> num;

cout << "Solid Rhombus" << endl;
for(i = 0; i < num; i++)
{
for(j = 0; j < num - i; j++)
{
cout << " "; 
}
for(j = 0; j < num; j++)
{
cout << "*";
}
cout << endl;
}



return 0;
}
