#include <iostream>
#include<string>
using namespace std;

void print(int n, string name){
    if(n == 0){
        return;
    }
    cout<<name<<endl;
    print(n-1, name);
}

int main() {
    char a[10] =  "garima";
    string garima = "garima";
    print(10, garima);
    
    return 0;
}
