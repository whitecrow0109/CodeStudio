#include <bits/stdc++.h> 

queue<int> reverseQueue(queue<int> q)
{
    queue<int> ans;
    vector<int> x;
    while(!q.empty()) {
        int ans = q.front();    q.pop();
        x.push_back(ans);
    }
    for (int i = x.size() - 1; i >= 0; i --) {
        ans.push(x[i]);
    }
    return ans;
}
