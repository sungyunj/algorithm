#include <iostream>
#include <fstream>
#include <cmath> // abs() 함수 사용을 위해 수정

using namespace std;

bool jollyJumper(int arr[], int n) {
    bool diff[3000] = {false}; // n-1까지의 차이를 체크하기 위한 배열

    for (int i = 0; i < n - 1; i++) {
        int absDiff = abs(arr[i] - arr[i+1]);

        if (absDiff < 1 || absDiff >= n || diff[absDiff]) {
            return false; // 조건에 맞지 않는 경우
        }
        diff[absDiff] = true;
    }

    return true;
}

int main() {
    ifstream inp("jolly.inp");
    ofstream out("jolly.out");

    int n;

    while (inp >> n) {
        int* sequence = new int[n];

        for (int i = 0; i < n; i++) {
            inp >> sequence[i];
        }

        if (jollyJumper(sequence, n)) {
            out << "Jolly" << endl;
        } else {
            out << "Not Jolly" << endl;
        }

        delete[] sequence;
    }

    inp.close();
    out.close();

    return 0;
}
