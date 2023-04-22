#include <iostream>

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
        
        
Node* takeIn(){
    int data;
    cin>>data;
    Node *head = NULL;
    Node *tail = NULL;
    while( data != -10000){
        Node *newNode = new Node(data);
        if(head == NULL){
            head = newNode;
            tail = newNode;
        }
        else{
            tail->next = newNode;
            tail = newNode;
        }
        cin>>data;
        
    }
    return head;
}
void print(Node *head){
    Node *temp = head;
    while(temp){
        cout<<temp->data<<" ";
        temp = temp->next;
    }
    cout<<endl;
}

void insert(Node* head, int i, int data){
    Node* temp = head;
    Node *newNode = new Node(data);
    int count = 0;
    while(count< i-1){
        temp = temp->next;
        count++;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}

Node* deleteNode(Node* head, int i){
    Node * temp = head;
    Node *curr = head;
    int count = 0;
    if(i == 0){
        head = temp->next;
        delete temp;
        return head;
    }
    while(count<i-1 && temp->next!= NULL){
        temp = temp->next;
        count++;
    }
    if(temp->next == NULL){
        return head;
    }
    else{
        curr = temp->next;
        temp->next = curr->next;
        delete curr;
        return head;
    }
}

int main()
{
    Node *head = takeIn();
    print(head);
    //head = deleteNode(head, 7);
    print(head);
    return 0;
}
