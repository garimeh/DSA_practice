#include<iostream>
using namespace std;

 class Node
        {
        public:
	        int data;
	        Node *next;
	        Node(int data)
	        {
		        this->data = data;
		        this->next = NULL;
	        }
        };


Node* merge2sortedll(Node* head1, Node* head2){
    if(head1 == NULL){
        return head2;
    }
    if(head2 == NULL){
        return head1;
    }
    Node* head = NULL;
    Node* tail = NULL;
    if(head1 == NULL && head2 == NULL){
        return head;
    }
    if(head1->data <= head2->data){
            head = head1;
            tail = head1;
            head1 = head1->next;
        }
    else if(head1->data > head2->data){
        head = head2;
        tail = head2;
        head2 = head2->next;
        }
    while(head1 != NULL && head2 != NULL){
        if(head1->data<= head2->data){
            tail->next = head1;
            tail = head1;
            head1 = head1->next;
        }
        else if(head1> head2){
            tail->next = head2;
            tail = head2;
            head2 = head2->next;
        }
    }
    if(head1 == NULL && head2 != NULL){
        while(head2 != NULL){
            tail->next = head2;
            tail = head2;
            head2 = head2->next;
        }
    }
    else if(head2 == NULL && head1 != NULL){
        while(head1 != NULL){
            tail->next = head1;
            tail = head1;
            head1 = head1->next;
        }
    }
    tail->next = NULL;
    return head;
}

int main(){
    int f;
    cin>>f;
    cout<<f;
    return 0;
}