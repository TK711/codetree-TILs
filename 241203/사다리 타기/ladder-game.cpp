#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Point {
    int from, order;
};

int n, m;
vector<Point> ladders;
int result[11];     // 초기 사다리 결과
int min_count = 15; // 최소 가로줄 개수
vector<Point> selected; // 선택된 가로줄 리스트

bool cmp(Point a, Point b) {
    if (a.order == b.order) {
        return a.from < b.from;
    }
    return a.order < b.order;
}


bool is_valid() {
    for (int i = 1; i <= n; i++) {
        int pos = i; 
        for (auto ladder : selected) {
            if (pos == ladder.from) {
                pos = ladder.from + 1;
            } else if (pos == ladder.from + 1) {
                pos = ladder.from;
            }
        }
        if (pos != result[i]) return false; 
    }
    return true;
}

void dfs(int idx, int cnt) {
    
    if (cnt >= min_count) return;

    if (is_valid()) {
        min_count = cnt;
        return;
    }

    
    if (idx >= m) return;

   
    dfs(idx + 1, cnt);

   
    selected.push_back(ladders[idx]);
    dfs(idx + 1, cnt + 1);
    selected.pop_back(); /
}

void calculate_first() {
    for (int i = 1; i <= n; i++) {
        int pos = i; 
        for (auto ladder : ladders) {
            if (pos == ladder.from) {
                pos = ladder.from + 1;
            } else if (pos == ladder.from + 1) {
                pos = ladder.from;
            }
        }
        result[pos] = i; 
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        ladders.push_back({a, b});
    }

    sort(ladders.begin(), ladders.end(), cmp);

    calculate_first(); 
    dfs(0, 0);         
    cout << min_count << "\n"; 

    return 0;
}
