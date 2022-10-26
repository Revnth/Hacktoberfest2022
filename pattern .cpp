#include <iostream>
using namespace std;
int main() {
int n = 4; ​ ​//Number of rows taken input
int i = 1; ​ // for iterating over rows starting from the first row
while(i < n) {
 int j = 1; ​// for iterating over columns
 while(j <= i) { ​// since for each column row, we will be iterating
 // over each column
 cout << j;
 j = j + 1; ​// as we have discussed above that i-th row will
 // have i columns
}
 cout << endl;
i++;​// for iterating over each row
}
}
