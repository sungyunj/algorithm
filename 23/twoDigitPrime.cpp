#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i <= sqrt(num); i += 6) {
        if (num % i == 0 || num % (i + 2) == 0)
            return false;
    }
    return true;
}

int main() {
    ifstream inp("twoDigitPrime.inp");
    ofstream out("twoDigitPrime.out");
    
    int T;
    inp >> T;
    
    vector<int> twoDigitPrime;
    for (int i = 10; i < 100; ++i) {
        if (isPrime(i)) {
            twoDigitPrime.push_back(i);
        }
    }

    while (T--) {
        int a, b;
        inp >> a >> b;
        int count = 0;

        for (int num = a; num <= b; ++num) {
            string numStr = to_string(num);
            bool isFound = false;
            for (size_t i = 0; i < numStr.size() && !isFound; ++i) {
                for (size_t j = i + 1; j < numStr.size() && !isFound; ++j) {
                    int num1 = (numStr[i] - '0') * 10 + (numStr[j] - '0');
                    int num2 = (numStr[j] - '0') * 10 + (numStr[i] - '0');
                    if (find(twoDigitPrime.begin(), twoDigitPrime.end(), num1) != twoDigitPrime.end() ||
                        find(twoDigitPrime.begin(), twoDigitPrime.end(), num2) != twoDigitPrime.end()) {
                        isFound = true;
                    }
                }
            }
            if (isFound) {
                count++;
            }
        }

        out << count << endl;
    }

    inp.close();
    out.close();

    return 0;
}
