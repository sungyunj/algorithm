#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

struct Node {
    int num;
    int left, right;
};

int n;
int list[1001];
int idx[1001];
char c[2001];
Node nodes[1001];

int bracketLen;
int bracketIdx = 0;
int nextNode = 0;

void build(int currentNode) {
    int prev = 0;
    while (bracketIdx < bracketLen) {
        if (prev == 0) {
            if (c[bracketIdx] == '(') {
                nodes[currentNode].left = nextNode;
                bracketIdx++;
                nextNode++;
                build(nextNode - 1);
            } else {
                bracketIdx++;
            }
            prev++;
        } else {
            if (c[bracketIdx] == '(') {
                nodes[currentNode].right = nextNode;
                bracketIdx++;
                nextNode++;
                build(nextNode - 1);
            } 
            else {
                bracketIdx++;
            }
            return;
        }
    }
}

void build_bracket(int start, int end, int range[]) {
    int target = idx[nextNode];
    int left = target - range[0];
    int right = range[1] - target;

    c[start] = '(';
    c[start + 1 + left * 2] = ')';

    if (left > 0) {
        int left_range[2] = { range[0], target - 1 };
        nextNode++;

        build_bracket(start + 1, start + left * 2, left_range);
    }
    if (right > 0) {
        int right_range[2] = { target + 1, range[1] };
        nextNode++;

        build_bracket(start + left * 2 + 2, end, right_range);
    }
}

void dfs(int currentNode, ofstream& out) {
    if (nodes[currentNode].left != 0) dfs(nodes[currentNode].left, out);

    out << currentNode + 1 << " ";

    if (nodes[currentNode].right != 0) dfs(nodes[currentNode].right, out);
}

void clear() {
    for (int i = 0; i < nextNode; i++) {
        nodes[i].left = 0;
        nodes[i].right = 0;
    }

    fill(c, c + n * 2, '\0');
}

int main() {
    ifstream inp("transform.inp");
    ofstream out("transform.out");

    int T;
    inp >> T;

    while (T--) {

        int k;
        inp >> n >> k;

        if (k == 1) {
            inp >> c;

            bracketLen = n * 2;
            bracketIdx = 1;
            nextNode = 1;
            build(0);

            out << n << " ";
            dfs(0, out);
            out << endl;
        } 
        else {
            for (int i = 0; i < n; i++) {
                inp >> list[i];
                idx[list[i]] = i;
            }
            nextNode = 1;
            int range[2] = { 0, n - 1 };
            build_bracket(0, n * 2 - 1, range);

            out << n << " " << c << endl;
        }
        clear();
    }

    inp.close();
    out.close();

    return 0;
}
