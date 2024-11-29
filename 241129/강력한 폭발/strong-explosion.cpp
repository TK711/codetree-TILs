#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define First ios::sync_with_stdio(0); cout.tie(0); cin.tie(0);

int arr[21][21];          // 격자의 초기 상태
bool bombed[21][21];      // 폭탄 피해 여부를 기록하는 배열
int n;                    // 격자의 크기
vector<pair<int, int>> bomb_place; // 폭탄 위치 저장
int bomb_shape[4][5][2] = {
    {}, 
    {{-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}},      
    {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {0, 0}},     
    {{-1, -1}, {1, 1}, {1, -1}, {-1, 1}, {0, 0}}    
};

int ans = 0; 


void validBomb(int x, int y, int type) {
    for (int i = 0; i < 5; i++) {
        int nx = x + bomb_shape[type][i][0];
        int ny = y + bomb_shape[type][i][1];
        if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue; // 격자 범위 초과 시 무시
        bombed[nx][ny] = true; 
    }
}


int calculate() {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (bombed[i][j]) cnt++; 
        }
    }
    return cnt;
}

// 폭탄 배치 탐색 (백트래킹)
void play(int cnt) {
    // 폭탄을 모두 배치한 경우
    if (cnt == bomb_place.size()) {
        ans = max(ans, calculate()); // 최대 피해 영역 갱신
        return;
    }

    // 현재 폭탄 위치 가져오기
    int x = bomb_place[cnt].first;
    int y = bomb_place[cnt].second;
    bool temp[21][21];

    // 1, 2, 3번 폭탄 배치하며 탐색
    for (int i = 1; i <= 3; i++) {
        
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                temp[j][k] = bombed[j][k];
            }
        }

        validBomb(x, y, i); 
        play(cnt + 1);     

        // `bombed` 상태 복원
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                bombed[j][k] = temp[j][k];
            }
        }
    }
}

int main() {
    cin >> n;

   
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 1) {
                bomb_place.push_back({i, j});
            }
        }
    }

    // 백트래킹 시작
    play(0);

    // 결과 출력
    cout << ans << "\n";
    return 0;
}
