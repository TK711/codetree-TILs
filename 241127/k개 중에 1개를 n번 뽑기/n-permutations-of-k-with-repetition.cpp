#include <iostream>
#include <vector>

using namespace std;
#define First ios::sync_with_stdio(0); cout.tie(0); cin.tie(0);

vector<int> ans;
int K, N;

void choose(int cur) {
    if (ans.size() == N) { 
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << ' ';
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= K; i++) {
        ans.push_back(i);
        choose(cur + 1);
        ans.pop_back(); 
    }
}

int main() {
    First
    cin >> K >> N; 
    choose(0); 
    return 0;
}2019181721222324252627282930
        choose(cur + 1);
        ans.pop_back(); 
    \}
\}

int main() {
    First
    cin >> K >> N; 
    choose(0); 
    return 0;

10void choose(int cur) {
$0
