#include <bits/stdc++.h>

vector<vector<long long int>> printPascal(int n) 
{
  vector<vector<long long int>> ans;
  vector<long long int> now;
  now.push_back(1);
  ans.push_back(now);
  for (int i = 1; i < n; i ++) {
    now.clear();
    for (int j = 0; j < i; j ++) {
      long long int val = ans[i - 1][j];
      if (j) val += ans[i - 1][j - 1];
      now.push_back(val);
    }
    now.push_back(1);
    ans.push_back(now);
  }
  return ans;
}