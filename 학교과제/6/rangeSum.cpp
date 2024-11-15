#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream inp("rangeSum.inp");
    ofstream out("rangeSum.out");

    long long n;
    inp >> n;

    vector<long long> A(n+1);

    for (long long i = 1; i <= n; i++) {
        inp >> A[i];
    }

    char c;
    while (inp >> c) {
        if (c == 'c') {
            long long a, b;
            inp >> a >> b;
;
            A[a] = b; 
        }
        else if (c == 's') {
            long long a, b;
            inp >> a >> b;
            long long sum = 0;
            for (long long i = a; i <= b; i++) {
                sum += A[i];
            }
            out << sum << endl;
        }
        else if (c == 'q') {
            break;
        }
    }

    inp.close();
    out.close();

    return 0;
}
