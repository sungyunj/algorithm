#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

// 최대공약수를 구하는 함수
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long t = b;
        b = a % b;
        a = t;
    }
    return a;
}

// 피타고라스 삼조를 찾는 함수
vector<pair<long long, long long> > pythagorean(long long L) {
    vector<pair<long long, long long> > triple;
    for (long long m = 2; m * m < L; ++m) {
        for (long long n = 1; n < m; ++n) {
            if ((m - n) % 2 == 1 && gcd(m, n) == 1) {
                long long a = m * m - n * n;
                long long b = 2 * m * n;
                long long c = m * m + n * n;
                if (2 * (a + b) <= L) {
                    triple.push_back(make_pair(min(a, b), max(a, b)));
                }
            }
        }
    }
    return triple;
}

// 비교 함수
bool compare(const pair<long long, long long>& a, const pair<long long, long long>& b) {
    return a.first + a.second < b.first + b.second;
}

int main() {
    ifstream inp("rectangles.inp");
    ofstream out("rectangles.out");
    int T;
    inp >> T;
    while (T--) {
        long long L;
        inp >> L;
        vector<pair<long long, long long> > triple = pythagorean(L);
        sort(triple.begin(), triple.end(), compare);

        int count = 0;
        for (size_t i = 0; i < triple.size(); ++i) {
            long long perimeter = 2 * (triple[i].first + triple[i].second);
            if (L >= perimeter) {
                L -= perimeter;
                count++;
            } else {
                break;
            }
        }
        out << count << endl;
    }
    inp.close();
    out.close();
    return 0;
}
