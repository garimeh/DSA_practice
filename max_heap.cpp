#include<iostream>

using namespace std;

void swap(int *i, int *j){
    int temp = *i;
    *i = *j;
    *j = temp;
}

class maxHeap{
    int *h;
    int cap;
    int size;
    public:
    maxHeap(int cap);
    int parent(int i){
        return i/2;
    }
    int left(int i){
        return 2*i;
    }
    int right(int i){
        return (2*i+1);
    }
    void insert(int val);

};

maxHeap::maxHeap(int cap){
    this->cap = cap;
    h = new int[cap];
    size = 0;
}
void maxHeap::insert(int val){
    if(size == cap){
        cout<<"heap is full!!"<<endl;
        return
    }
    int i = size;
    size++;
    h[i] = val;

    while(i!=0 && h[parent(i)]< h[i]){
        swap(&h[parent(i)],&h[i]);
        i = parent(i);
    }
}
int main(){
   
return 0;
}