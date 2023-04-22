#include <iostream>
using namespace std;

void selection(int arr[], int n){
    int start = 0, i, temp, min, mind;
    for(; start<n - 1; start++){
        min = arr[start];
        mind = start;
        for(i = start + 1; i < n; i++){
            if(arr[i]<min){
                min = arr[i];
                mind = i;
            }
        }
        temp = arr[mind];
        arr[mind] = arr[start];
        arr[start] = temp;
    }
    
}

int main() {
    int n;
    int arr[100];
    cin>>n;
    for(int i = 0; i < n; i++){
        cin>>arr[i];
    }
    selection(arr, n);
    for(int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}