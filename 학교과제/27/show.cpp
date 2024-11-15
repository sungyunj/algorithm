#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

struct Guess {
    int bulb1, bulb2, bulb3;
    char color1, color2, color3;
};

class TwoSat {
public:
    explicit TwoSat(int n) : n(n), list(2 * n), revList(2 * n), solution(n, -1) {}

    void addVariable(int x, bool xVal, int y, bool yVal) {
        int u = 2 * x + xVal;
        int v = 2 * y + yVal;
        list[u ^ 1].push_back(v);
        list[v ^ 1].push_back(u);
        revList[v].push_back(u ^ 1);
        revList[u].push_back(v ^ 1);
    }

    bool solve() {
        vector<int> order, sccIndex(2 * n, -1);
        vector<bool> visited(2 * n, false);
        for (int i = 0; i < 2 * n; ++i)
            if (!visited[i])
                dfs1(i, visited, order);

        reverse(order.begin(), order.end());

        int cmp = 0;
        for (int u : order)
            if (sccIndex[u] == -1)
                dfs2(u, cmp++, sccIndex);

        for (int i = 0; i < n; ++i)
            if (sccIndex[2 * i] == sccIndex[2 * i + 1])
                return false;

        for (int i = 0; i < n; ++i)
            solution[i] = (sccIndex[2 * i] > sccIndex[2 * i + 1]);

        return true;
    }

    const vector<bool>& getSolution() const { return solution; }

private:
    int n;
    vector<vector<int>> list, revList;
    vector<bool> solution;

    void dfs1(int u, vector<bool>& visited, vector<int>& order) {
        visited[u] = true;
        for (int v : list[u])
            if (!visited[v])
                dfs1(v, visited, order);
        order.push_back(u);
    }

    void dfs2(int u, int cmp, vector<int>& sccIndex) {
        sccIndex[u] = cmp;
        for (int v : revList[u])
            if (sccIndex[v] == -1)
                dfs2(v, cmp, sccIndex);
    }
};

bool satisfy(int k, const vector<Guess>& Guesss) {
    TwoSat solver(k + 1);

    for (const auto& p : Guesss) {
        bool color1 = (p.color1 == 'R');
        bool color2 = (p.color2 == 'R');
        bool color3 = (p.color3 == 'R');

        solver.addVariable(p.bulb1, !color1, p.bulb2, !color2);
        solver.addVariable(p.bulb1, !color1, p.bulb3, !color3);
        solver.addVariable(p.bulb2, !color2, p.bulb3, !color3);
    }

    return solver.solve();
}

int main() {
    ifstream inp("show.inp");
    ofstream out("show.out");

    int T;
    inp >> T;

    while (T--) {
        int k, N;
        inp >> k >> N;

        vector<Guess> Guesss(N);

        for (int i = 0; i < N; ++i) {
            inp >> Guesss[i].bulb1 >> Guesss[i].color1
                >> Guesss[i].bulb2 >> Guesss[i].color2
                >> Guesss[i].bulb3 >> Guesss[i].color3;
        }

        if (satisfy(k, Guesss)) {
            out << 1 << endl;
        } else {
            out << -1 << endl;
        }
    }

    inp.close();
    out.close();

    return 0;
}
