#include <iostream>
#include <vector>
using namespace std;

int n, t;
vector<int> v;

void input(){
    cin >> n >> t;
    v.resize(n);
    for(int i=0; i<n; i++){
        cin >> v[i];
    }
}

int main() {
    input();
    
    int max_len = 0;  // 연속 부분 수열의 최대 길이 저장
    int current_len = 0;  // 현재 연속 부분 수열의 길이

    for(int i=0; i<n; i++){
        if (v[i] > t) {
            current_len++;  // t보다 큰 숫자가 나오면 길이를 증가
        } else {
            max_len = max(max_len, current_len);  // t보다 큰 수열이 끝나면 최대 길이 갱신
            current_len = 0;  // 연속 부분 수열 길이 초기화
        }
    }
    // 마지막 연속 수열 체크
    max_len = max(max_len, current_len);

    cout << max_len << "\n";  // 결과 출력
}