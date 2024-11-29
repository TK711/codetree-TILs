#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define First ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int n, ans; 
vector<pair<int, int>> v;

bool cmp(pair<int,int> a, pair<int,int> b){
    if(a.second == b.second){
        return a.first < a.second;
    }
    return a.second < b.second;
}


void dfs(int idx, int cnt, int last_y) {
    // 모든 선분을 확인한 경우
    if (idx == n) {
        ans = max(ans, cnt); // 최대값 갱신
        return;
    }

   
    dfs(idx + 1, cnt, last_y);

   
    if (last_y < v[idx].first) { 
        dfs(idx + 1, cnt + 1, v[idx].second);
    }
}

int main() {
    First

    // 입력
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }

    
    sort(v.begin(),v.end(),cmp);


    dfs(0, 0, 0);

    // 출력
    cout << ans << "\n";

    return 0;
}
