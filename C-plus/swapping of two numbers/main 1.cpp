#include <iostream>
using namespace std;
int main(){
    int a,b;
    cout<<"Enter the value of a : ";
    cin>>a;
    cout<<"Enter the value of b : ";
    cin>>b;
    a+=b;b = a-b;a-=b;
    cout<<"after swapping a = "<<a<<", b = "<<b;
}
