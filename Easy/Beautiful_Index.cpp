#include <bits/stdc++.h> 
int beautifulIndex(int N, vector<int> A)
{
	vector<long long> sum(N + 5);
	sum[0] = 0;
	for (int i = 1; i <= N; i ++) {
		sum[i] = sum[i - 1] + A[i - 1];
	}
	for (int i = 1; i <= N; i ++) {
		if (sum[i - 1] == sum[N] - sum[i]) return i;
	}
	return -1;
}