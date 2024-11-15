#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const long long MOD = 1000000007;

struct Matrix2x2 {
    long long matrix[2][2];
};

Matrix2x2 multiMat(Matrix2x2 a, Matrix2x2 b) {
    Matrix2x2 result;
    result.matrix[0][0] = (a.matrix[0][0] * b.matrix[0][0] + a.matrix[0][1] * b.matrix[1][0]) % MOD;
    result.matrix[0][1] = (a.matrix[0][0] * b.matrix[0][1] + a.matrix[0][1] * b.matrix[1][1]) % MOD;
    result.matrix[1][0] = (a.matrix[1][0] * b.matrix[0][0] + a.matrix[1][1] * b.matrix[1][0]) % MOD;
    result.matrix[1][1] = (a.matrix[1][0] * b.matrix[0][1] + a.matrix[1][1] * b.matrix[1][1]) % MOD;
    return result;
}

Matrix2x2 matPow(Matrix2x2 baseMatrix, long long exp) {
    Matrix2x2 result = {{{1, 0}, {0, 1}}};
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = multiMat(result, baseMatrix);
        }
        baseMatrix = multiMat(baseMatrix, baseMatrix);
        exp /= 2;
    }
    return result;
}

long long fibo(long long n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    Matrix2x2 baseMatrix = {{{1, 1}, {1, 0}}};
    Matrix2x2 result = matPow(baseMatrix, n - 1);
    return result.matrix[0][0];
}

int main() {
    ifstream inp("bigFibonacci.inp");
    ofstream out("bigFibonacci.out");
    
    int T;
    inp >> T;
    vector<long long> value(T);
    for (int i = 0; i < T; ++i) {
        inp >> value[i];
    }
    
    for (int i = 0; i < T; ++i) {
        long long n = value[i];
        long long fiboMod = fibo(n) % MOD;
        out << n << " " << fiboMod << endl;
    }
    
    inp.close();
    out.close();
    
    return 0;
}
