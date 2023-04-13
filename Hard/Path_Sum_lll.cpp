#include <bits/stdc++.h> 

template <typename T>
class TreeNode {
   public:
    T data;
    TreeNode<T> *left;
    TreeNode<T> *right;

    TreeNode(T data) {
        this->data = data;
        left = NULL;
        right = NULL;
    }
};

int ans;

void DFS(TreeNode<int> *rt, int k, int sum, int tf) {
    if (sum == k && tf) ans ++;
    if (tf == 0) { 
        if (rt->left) {
            DFS(rt->left, k, 0, 0);
            DFS(rt->left, k, rt->left->data, 1);
        }
        if (rt->right) {
            DFS(rt->right, k, 0, 0);
            DFS(rt->right, k, rt->right->data, 1);
        }
    } else {
        if (rt->left) {
            DFS(rt->left, k, sum + rt->left->data, 1);
        }
        if (rt->right) {
            DFS(rt->right, k, sum + rt->right->data, 1);
        }
    }
}

int noWays(TreeNode < int > * root, int k) {
    ans = 0;
    if (root) {
        DFS(root, k, 0, 0);
        DFS(root, k, root->data, 1);
    }
    return ans;
}

