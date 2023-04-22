#include<iostream>
using namespace std;


int main(){
    int n;
    cin>>n;
    int i = 1;
    int stars = 1, mid = (n+1)/2;
    while(i<=mid ){
        int spaces = 1;
    	while(spaces<= mid-i){
            cout<<" ";
            spaces = spaces + 1;
        }
        int j = 1;
        while(j <= 2*i - 1){
            cout<<"*"; 
            j = j + 1;
        }
        cout<<endl;
        i = i + 1;
    }

    for(int k = mid - 1; k >= 1; --k)
    {
        for(int space = 1; space < mid-k+1; ++space)
            cout << " ";

        for(int j = 1; j <= 2*k-1; ++j)
            cout << "*";

        cout << endl;
    }
}







