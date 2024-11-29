#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define First ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int n;
vector<pair<int, int>> v;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second) {
        return a.first < b.first;
    }
    return a.second < b.second;
}

int main() {
    First


    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }

 
    sort(v.begin(), v.end(), cmp);

    vector<int> dp(n, 1);


    for (int i = 1; i < n; i++) {
        dp[i] = dp[i - 1]; 
        for (int j = 0; j < i; j++) {
            if (v[j].second < v[i].first) { 
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    
    cout << dp[n - 1] << "\n";

    return 0;
}
