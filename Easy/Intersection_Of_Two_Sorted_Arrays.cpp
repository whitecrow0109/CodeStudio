#include <bits/stdc++.h> 

vector<int> findArrayIntersection(vector<int> &arr1, int n, vector<int> &arr2, int m)
{
	const int N = 100005;
	int x[N] = {0}, y[N] = {0};
	for (int i = 0; i < n; i ++) x[arr1[i]] ++;
	for (int i = 0; i < m; i ++) y[arr2[i]] ++;
	vector<int> ans;
	for (int i = 0; i < N; i ++) {
		for (int j = 0; j < min(x[i], y[i]); j ++) ans.push_back(i);
	}
	return ans;
}