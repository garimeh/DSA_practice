#include <iostream>
using namespace std;

int main(){

    int n;
    cin>>n;
    if((n>=1)&&(n<=100)){
        for(int i = 2; i <= n;){
            if( i == 2){
                cout<<2<<endl;
                i++;
        }
            if(i == 3){
                cout<<3<<endl;
                i++;
        }
        if(i>3)
            for(int d = 2; d < i; d++) {
                if(i%d==0){
                    continue;
                }
                else{
                    cout<<i<<endl;
                }
            }
        }
    }
  
}



