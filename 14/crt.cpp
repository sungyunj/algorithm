#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

// 최대 공약수를 재귀적으로 계산하는 함수
long long GCD(long long x, long long y){
    if(y == 0) {
        return x;
    }
    else {
        return GCD(y, x % y);
    }
}

// 확장된 유클리드 알고리즘을 사용하여 모듈라 역을 찾는 함수
long long Euclid(long long ori_x, long long ori_y){
    long long x = ori_x, y = ori_y, p;
    long long x_update, x_update1 = 1, x_update2 = 0;
    long long y_update, y_update1 = 0, y_update2 = 1;
    long long z;
    while(y > 0){
        z = x / y;
        p = x - z * y;
        x = y;
        y = p;

        x_update = x_update1 - z * x_update2;
        x_update1 = x_update2;
        x_update2 = x_update;

        y_update = y_update1 - z * y_update2;
        y_update1 = y_update2;
        y_update2 = y_update;
    }
    return x_update1;
}

int main(){
    ifstream inp("1.inp");
    ofstream out("crt.out");

    int T;
    inp >> T;

    while(T > 0){
        vector<long long> v1;
        vector<long long> v2;
        long long coeff = 1; // 계수
        long long cons = 0; // 상수
        int n;
        inp >> n;
        for (int i = 0; i < n; i++) {
            long long a, b;
            inp >> a >> b;
            v1.push_back(a);
            v2.push_back(b);
        }
        long long sum = 1;
        long long a=0, b=0, c=0;
        bool flag = false;
        for (int i = 0; i < n; i++) {
            a = sum, b = v1[i], c = v2[i];

            // 해가 존재하는지 검증하기 위해 gcd 조건을 확인
            if (b % GCD(a, c) != 0) {
                flag = true; break;
            }

            // 계산을 단순화하기 위해 gcd로 숫자들을 축소
            long long temp = GCD(GCD(a, b), c);
            a /= temp; b /= temp; c /= temp;

            // 오버플로우를 피하기 위해 modulus 수행
            a %= c; b %= c;

            // 모듈로 c에 대한 a의 모듈라 역을 계산
            long long rA = Euclid(a, c);
            b = b * rA % c;

            // b가 음수가 아니도록 보장
            if (b < 0) {
                b += c;
            }

            // 결과의 상수 부분을 업데이트
            cons += coeff * b;
            coeff = coeff * c;

            // 누적된 결과를 고려하여 다음 나머지를 조정
            v1[i+1] = v1[i + 1] - cons;
            sum = coeff;

            // 다음 나머지를 해당 모듈로 내에서 정규화
            if (i != n - 1) {
                v1[i + 1] %= v2[i + 1];
                if (v1[i + 1] < 0) v1[i + 1] += v2[i + 1];
            }
        }
        // 해결할 수 없는 경우 처리
        if (flag) out << "-1" << endl;
        else out << cons << endl;
        T--;
    }

    inp.close();
    out.close();
}
