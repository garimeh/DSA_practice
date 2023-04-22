#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int arr[n];
    bool isInc = false, invalid = false;
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }
    int i = 0;
    while(i<n){
        if(arr[i]>arr[i+1]){
            isInc = false;
            invalid = false;
            i++;
        }
        else if(arr[i]<arr[i+1]){
            isInc = true;
            invalid = false;
            i++;
            
        }
        else if((isInc == true)&&(arr[i]>=arr[i+1])){
            invalid = true;
            break;
        }
    }
    if(invalid){
        cout<<"false";
    }
    else{
        cout<<"true";
    }
    return 0;
}