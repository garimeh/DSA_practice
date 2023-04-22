#include<iostream>
#include<cstdlib>
#include<vector>

using std::vector;
using std::cin;
using std::cout;

 long long maxpairwiseprod(vector<int> numbers) 
    {
        long long result = 0;
        int n = numbers.size();
        for(int i = 0;i < n; i++){
            for (int j = i+1 ; j < n; j++)
            {
                if (((long long)numbers[i])*numbers[j] > result)
                {
                    result = ((long long)numbers[i])*numbers[j];
                }
                
            }
            
        }
        return result;
    }


int main(){

   vector<int> arr[10];

   long long res = maxpairwiseprod(arr);

    cout<<res;

    return 0;
}