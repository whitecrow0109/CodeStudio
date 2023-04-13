#include <bits/stdc++.h>

using namespace std;

const int N = 11;
vector<vector<int>> ans;
int x[N];

void dfs(int st, int cnt, int now, int k, int sum) {
	if (now > sum) return;
	if (cnt == k) {
		if (now == sum) {
			vector<int> S;
			for (int i = 0; i < cnt; i ++) S.push_back(x[i]);
			ans.push_back(S);
			return;
		}
		return;
	}
	for (int i = st + 1; i <= 9; i ++) {
		x[cnt] = i;
		dfs(i, cnt + 1, i + now, k, sum);
	}
}

vector<vector<int>> combinationSum3(int k, int n) {
	ans.clear();
	dfs(0, 0, 0, k, n);
	return ans;
}

int main() {
	int ncase;
	for (cin >> ncase; ncase --; ) {
		int m, n;	cin >> m >> n;
		vector<vector<int>> ans = combinationSum3(m, n);
		for (auto u : ans) {
			for (int i = 0; i < u.size(); i ++) {
				if (i) cout << " ";
				cout << u[i];
			}
			cout << endl;
		}
	}	
}
