#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    // 데이터 읽기
    freopen("trip.inp", "r", stdin);
    freopen("trip.out", "w", stdout);

    int n;
    while (true) {
        cin >> n;
        if (n == 0)
            break;

        vector<double> expenses(n);
        double total = 0.0;

        // 각 학생의 비용을 입력 받고 총 비용을 계산
        for (int i = 0; i < n; ++i) {
            cin >> expenses[i];
            total += expenses[i];
        }

        // 평균 비용을 계산
        double average = total / n;

        // 각 학생의 비용과 평균 비용의 차이를 계산, 양수와 음수를 나눔
        double pos_diff = 0.0, neg_diff = 0.0;
        for (int i = 0; i < n; ++i) {
            double diff = (double)(long)((expenses[i] - average) * 100.0) / 100.0;
            if (diff > 0)
                pos_diff += diff;
            else
                neg_diff -= diff; // 음수 값은 양수로 변환하여 처리
        }

        // 모든 학생이 평균 비용을 지출하지 않은 경우, 각 학생의 비용을 모두 고려하여 최소 교환 금액을 계산
        double min_exchange = max(pos_diff, neg_diff);

        // 출력 형식에 맞게 최소 교환 금액을 출력
        cout << fixed << setprecision(2) << "$" << min_exchange << endl;
    }

    return 0;
}
