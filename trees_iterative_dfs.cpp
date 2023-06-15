#include<vector>
#include<stack>
#include<queue>
#include<iostream>
using namespace std;

class treenode{
    public:
    int val;
    treenode* left;
    treenode*right;
    treenode(){
        val = 0;
        right = nullptr;
        left = nullptr;
    }
    treenode(int x){
        val = x;
        right = nullptr;
        left = nullptr;
    }
    treenode(int x,treenode*l, treenode*r){
        val = x;
        right = r;
        left = l;
    }
    // vector<int> preorderi(treenode*);
};

vector<int> preorderi(treenode* root){
    vector<int> p;
    if (root == NULL) return p;
    stack<treenode*> st;
    st.push(root);
    while (!st.empty()){
        root = st.top();
        st.pop();
        p.push_back(root->val);
        if(root->right != NULL) st.push(root->right);
        if(root->left!= NULL) st.push(root->left);
    }
    return p;
    }
vector<int> inorderi(treenode* root){
    stack<treenode*> st;
    treenode* node = root;
    vector<int> i;
    while(true){
        if(node!=NULL){
            st.push(node);
            node = node->left;
        }
        else{
            if(st.empty()){
                break;
            }
            node = st.top();
            st.pop();
            i.push_back(node->val);
            node = node->right;
        }
    }
    return i;
}

vector<int> postorderi(treenode* root){
    vector<int> p;
    if(root==NULL) return p;
    stack<treenode*> st1, st2;
    st1.push(root);
    while(!st1.empty()){
        root = st1.top();
        st1.pop();
        st2.push(root);
        if(root->left!=NULL){
            st1.push(root->left);
        }
        if(root->right!=NULL){
            st1.push(root->right);
        }
    }
    while(!st2.empty()){
        p.push_back(st2.top()->val);
        st2.pop();
    }
    return p;
}
int main(){
   treenode* a = new treenode(1);
   a->left = new treenode(2);
   a->right = new treenode(3);
   a->left->left = new treenode(4);
   a->left->right = new treenode(5);
   a->right->left = new treenode(6);
   a->right->right = new treenode(7);
   vector<int> ans = postorderi(a);
   for(int i = 0; i<ans.size(); i++){
    cout<<ans[i]<<endl;
   }
return 0;
}
