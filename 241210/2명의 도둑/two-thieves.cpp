#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define First ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

int N, M, C;
int arr[11][11];


int calculateMaxValue(vector<int> weights) {
    int maxValue = 0;
    int len = weights.size();
  
    for (int subset = 1; subset < (1 << len); subset++) {
        int weightSum = 0;
        int valueSum = 0;
        for (int i = 0; i < len; i++) {
            if (subset & (1 << i)) {
                weightSum += weights[i];
                valueSum += weights[i] * weights[i];
            }
        }
        if (weightSum <= C) {
            maxValue = max(maxValue, valueSum);
        }
    }
    return maxValue;
}


int getMaxRowValue(int row, int startCol) {
    vector<int> weights;
    for (int j = startCol; j < startCol + M; j++) {
        weights.push_back(arr[row][j]);
    }
    return calculateMaxValue(weights);
}

int main() {
    First;
    cin >> N >> M >> C;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    int maxTotalValue = 0;


    for (int row1 = 0; row1 < N; row1++) {
        for (int row2 = row1; row2 < N; row2++) {
 
            for (int col1 = 0; col1 <= N - M; col1++) {
                int maxValue1 = getMaxRowValue(row1, col1);
                for (int col2 = 0; col2 <= N - M; col2++) {
             
                    if (row1 == row2 && col1 + M > col2) continue;

                    int maxValue2 = getMaxRowValue(row2, col2);
                    maxTotalValue = max(maxTotalValue, maxValue1 + maxValue2);
                }
            }
        }
    }

    cout << maxTotalValue << "\n";

    return 0;
}
