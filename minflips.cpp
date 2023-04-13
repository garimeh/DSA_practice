
#include <string>
#include<iostream>
using namespace std;

int minflips(string target){
    string init = "";
    for(int i = 0; i<target.length(); i++){
        init.push_back('0');
    }
    int count = 0;
    for(int i = 0; i < target.length(); i++){
        if(init[i] != target[i]){
            count++;
            for(int j = i; j<target.length(); j++){
                if(init[j] == '0'){
                    init[j] = '1';
                }
                else{
                    init[j] = '0';
                }
            }
        }
    }
    return count;
}

int main() {
    cout<<minflips("01011");

    return 0;
}