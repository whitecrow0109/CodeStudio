#include <bits/stdc++.h> 
const int N = 1005;

bool dp[N];

bool subsetSumToK(int n, int k, vector<int> &arr) {
    memset(dp, false, sizeof dp);
    dp[0] = true;
    for (int i = 0; i < n; i ++) {
        for (int j = k; j >= arr[i]; j --) {
            if (dp[j - arr[i]]) dp[j] = 1;
        }
    }
    return dp[k];
}