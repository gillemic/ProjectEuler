#include <iostream>
using namespace std;
 
int main()
{
    int a = 0, b = 1;
    int c, answer = 0;
    do{
        c = a + b;
        a = b;
        b = c;
        if(b%2==0){answer = answer + b;}
    } while(b<=4000000);
    cout << "Answer is " << answer << endl;
    return 0;
}