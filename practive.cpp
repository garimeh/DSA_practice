#include<iostream>
using namespace std;
#include "queues_array.h"


int main(){
   queue_arr<int> Q(10);
   Q.enqueue(10);
   Q.enqueue(20);
   Q.enqueue(30);
   cout<<Q.front();
   Q.enqueue(40);
   Q.enqueue(50);
   Q.dequeue();
   cout<<Q.front();
   Q.enqueue(60);
   Q.enqueue(70);
   Q.enqueue(80);
return 0;
}