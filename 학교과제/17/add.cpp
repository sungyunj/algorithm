#include <iostream>
#include <fstream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ifstream inp("add.inp");
    ofstream out("add.out");

    int N;
    while (inp >> N && N != 0) {
        priority_queue<int, vector<int>, greater<int> > minheap;
        int number;

        for (int i = 0; i < N; i++) {
            inp >> number;
            minheap.push(number);
        }

        long long total = 0;
        while (minheap.size() > 1) {
            int first = minheap.top(); minheap.pop();
            int second = minheap.top(); minheap.pop();

            int sum = first + second;
            total += sum;
            minheap.push(sum);
        }

        out << total << endl;
    }

    inp.close();
    out.close();
    return 0;
}
