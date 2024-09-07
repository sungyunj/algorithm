#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int CycleLength(long long n) {
    int length = 1;
    while (n != 1) {
        if (n % 2 == 0)
            n /= 2;
        else
            n = 3 * n + 1;
        length++;
    }
    return length;
}

int maxCycleLength(long long start, long long end) {
    int maxCycle = 0;
    for (long long i = min(start, end); i <= max(start, end); ++i) {
        int currentCycle = CycleLength(i);
        maxCycle = max(maxCycle, currentCycle);
    }
    return maxCycle;
}

int main() {
    ifstream inputFile("3nplus1.inp");
    ofstream outputFile("3nplus1.out");

    long long start, end;
    while (inputFile >> start >> end) {
        int maxCycle = maxCycleLength(start, end);
        outputFile << start << " " << end << " " << maxCycle << endl;
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
