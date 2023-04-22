#include<iostream>

using namespace std;


class stack_arr{
    int *data;
    int next;
    int s;
    public:
        stack_arr(int size){
            data = new int[size];
            next = 0;
            s = size;
        }

        void push(int element){
            if(next < s){
                data[next] = element;
                next++;
            }
            else{
                cout<<"stack overflow!"<<endl;
            }
            
        }

        bool isEmpty(){
            return next == 0;
        }

        int pop(){
            if(isEmpty()){
                cout<<"stack underflow!"<<endl;
                return INT_MIN;
            }
            else{
                next--;
                return data[next];
            }
        }
        int size(){
            return next;
        }
        int top(){
            return data[next-1];
        }
};

int main(){
   stack_arr s(4);
   s.push(10);
   s.push(20);
   s.push(90);
   s.push(100);
   cout<<s.pop()<<endl;
   s.push(200);
   cout<<s.top();
return 0;
}