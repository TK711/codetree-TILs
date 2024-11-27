#include <iostream>
#include <vector>

using namespace std;
#define First ios::sync_with_stdio(0); cout.tie(0); cin.tie(0);
vector<int> v;
vector<int> ans;
int K,N;

void choose(int cur){
    if(cur == N+1){
        for(int i=0; i<ans.size(); i++){
            cout << ans[i] << ' ';
        }cout << "\n";
        return;
    }
    for(int i=1; i<=N; i++){
        ans.push_back(i);
        choose(cur + 1);
        ans.pop_back();
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    First
    cin >> K >> N;
    choose(1);



    return 0;
}