#include <bits/stdc++.h> 
/************************************************************

    Following is the linked list node structure:
    
    template <typename T>
    class Node {
        public:
        T data;
        Node* next;

        Node(T data) {
            next = NULL;
            this->data = data;
        }
    };

************************************************************/

const int N = 1e5 + 5;

Node<int>* addTwoLists(Node<int>* first, Node<int>* second) {
    string A = "", B = "";
    while(first) {
        A += first->data + '0';
        first = first->next;
    }
    while(second) {
        B += second->data + '0';
        second = second->next;
    }
    int n = max(A.length(), B.length());
    A = string(n - A.length(), '0') + A;
    B = string(n - B.length(), '0') + B;
    int D[N] = {0}, cnt = 0, r = 0;
    for (int i = n - 1; i >= 0; i --) {
        int c = (A[i] - '0') + (B[i] - '0') + r;
        D[cnt ++] = c % 10;
        r = c / 10;
    }
    if (r) D[cnt ++] = r;
    Node<int>* ret = new Node<int>(D[cnt - 1]);
    Node<int>* last = ret;
    for (int i = cnt - 2; i >= 0; i --) {
        last->next = new Node<int>(D[i]);
        last = last->next;
    }
    return ret;
}