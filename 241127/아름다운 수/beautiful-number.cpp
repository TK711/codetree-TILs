#include <iostream>
using namespace std;

int n;
int beautiful_count = 0;


void find_beautiful(int length, int last_digit, int count) {
    
    if (length == n) {
        if (count == last_digit) {
            beautiful_count++;
        }
        return;
    }
    
    
    if (count == last_digit) {
        
        for (int i = 1; i <= 4; i++) {
            find_beautiful(length + 1, i, 1);
        }
    } else {
       
        find_beautiful(length + 1, last_digit, count + 1);
    }
}

int main() {
    cin >> n;

   
    for (int i = 1; i <= 4; i++) {
        find_beautiful(1, i, 1);
    }

    cout << beautiful_count << endl;

    return 0;
}
