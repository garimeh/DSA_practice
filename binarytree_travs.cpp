#include <vector>
#include<queue>
#include<iostream>
using namespace std;

class Node{
public:
    int data;
    Node* left;
    Node *right;
    Node(int k){
        data = k;
        left = NULL;
        right = NULL;
    }
    void preorder(Node*);
    void inorder(Node*);
    void postorder(Node*);
    vector<vector<int> > levelorder(Node*);
};

void Node::preorder(Node* a){
    if(a == NULL){
        return;
    }
    cout<<a->data<<" ";
    preorder(a->left);
    preorder(a->right);
}

void Node::inorder(Node* a){
    if( a == NULL){
        return;
    }
    inorder(a->left);
    cout<<a->data<<" ";
    inorder(a->right);
}

void Node::postorder(Node *a){
    if(a == NULL){
        return;
    }
    postorder(a->left);
    postorder(a->right);
    cout<<a->data<<" ";
}

vector<vector<int> > Node::levelorder(Node *a){
    vector<vector<int> > ans;
    if(a == NULL){
        return ans;
    }
    queue<Node*> q;
    q.push(a);
    while(!q.empty()){
        int s = q.size();
        vector<int> l;
        for(int i = 0; i<s;i++){
            Node* f = q.front();
            q.pop();
            if(f->left!=NULL){
                q.push(f->left);
            }
            if(f->right!=NULL){
                q.push(f->right);
            }
            l.push_back(f->data);
        }
        ans.push_back(l);
    }
    return ans;
}

int main() {
    Node* a = new Node(1);
    a->left = new Node(2);
    a->right = new Node(3);
    a->left->left = new Node(4);
    a->left->right = new Node(5);
    a->left->right->left = new Node(8);
    a->right->left = new Node(6);
    a->right->right = new Node(7);
    a->right->right->left = new Node(9);
    a->right->right->right = new Node(10);
    a->preorder(a);
    cout<<endl;
    a->inorder(a);
    cout<<endl;
    a->postorder(a);
    cout<<endl;
    vector<vector<int> > ans = a->levelorder(a);
    for(auto it = ans.begin(); it != ans.end(); it++){
    for(auto elem : *it){
        cout<<elem<<" ";
    }
    // cout<<endl;
}
    return 0;
}
