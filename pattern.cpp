#include<iostream>
using namespace std;


int main() {
    int n;
    cin>>n;
    int mid = n/2 +1;
    int i = 1;
    int stars = 1;
    while(i <= mid){
        int spaces = 1;
        while(spaces <= mid - i){
            cout<<" ";
            spaces = spaces + 1;
        }
        int j = 1;
        while(j <= stars){
            cout<<"*";
            j = j + 1;
        }
        stars = stars + 2;
        cout<<endl;
        i = i + 1;
    }
    int k = mid;
    int star = n;
    while(k > 0 ){
        int space = 1;
        while(space <= mid - k){
            cout<<" ";
            space = space + 1;
        }
        int j = star;
        while(j > 0){
            cout<<"*";
            j = j - 1;
        }
        star = star - 2;
        cout<<endl;
        i = k - 1;
    }
}

