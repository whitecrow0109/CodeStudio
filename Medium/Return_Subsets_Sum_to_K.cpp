vector<vector<int>> findSubsetsThatSumToK(vector<int> arr, int n, int k)
{   
    vector<vector<int>> ans;
    for (int i = 1; i < (1 << n); i ++) {
        vector<int> lst;
        int sum = 0;
        for (int j = 0; j < n; j ++) {
            if ((1 << j) & i)  {
                sum += arr[j];
                lst.push_back(arr[j]);
            }
        }
        if (sum == k) ans.push_back(lst);
    }
    return ans;
}