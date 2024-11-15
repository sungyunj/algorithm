#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Graph {
public:
    int v;  // 정점의 수
    vector<vector<int> > edge;   // 그래프의 인접 리스트
    vector<vector<int> > edgeAll;  // 전치 그래프의 인접 리스트

    Graph(int v) : v(v), edge(v), edgeAll(v) {}

    // 그래프에 간선을 추가하는 함수
    void addEdge(int v, int w) {
        edge[v].push_back(w);
        edgeAll[w].push_back(v); // 전치 그래프에도 간선을 추가
    }

    // DFS 함수
    void DFS(int v, vector<bool>& visit, stack<int>& Stack) {
        visit[v] = true;

        // 이 정점에 인접한 모든 정점을 순회
        for (int i = 0; i < edge[v].size(); i++)
            if (!visit[edge[v][i]])
                DFS(edge[v][i], visit, Stack);

        // 모든 인접 정점을 방문한 후에 현재 정점을 스택에 푸시
        Stack.push(v);
    }

    // 강하게 연결된 컴포넌트를 찾고 그 수를 반환하는 함수
    int scc() {
        stack<int> Stack;

        // 모든 정점을 방문하지 않은 상태로 초기화
        vector<bool> visit(v, false);

        // 모든 정점을 한 번씩 방문하면서 완료 시간에 따라 스택에 푸시
        for (int i = 0; i < v; i++)
            if (!visit[i])
                DFS(i, visit, Stack);

        // 모든 정점의 방문 상태를 다시 초기화
        fill(visit.begin(), visit.end(), false);

        // 스택에서 정점을 하나씩 꺼내면서 전치 그래프에서 DFS 수행
        int count = 0;
        while (!Stack.empty()) {
            int v = Stack.top();
            Stack.pop();

            if (!visit[v]) {
                stack<int> dfsStack; // 더미 스택
                visitScc(v, visit, dfsStack);
                count++;  // 새로운 강하게 연결된 컴포넌트를 찾을 때마다 카운트 증가
            }
        }

        return count;
    }

    // 전치 그래프에 대한 DFS 함수
    void visitScc(int v, vector<bool>& visit, stack<int>& dfsStack) {
        visit[v] = true;

        // 전치 그래프에서 이 정점에 인접한 정점을 순회
        for (int i = 0; i < edgeAll[v].size(); i++)
            if (!visit[edgeAll[v][i]])
                visitScc(edgeAll[v][i], visit, dfsStack);
    }
};

int main() {
    ifstream inp("scc.inp");
    ofstream out("scc.out");
    int m, n;
    inp >> m >> n;  // 정점과 간선의 수 읽기

    Graph g(m);  // 그래프 객체 생성

    for (int i = 0; i < n; i++) {
        int u, v;
        inp >> u >> v;  // 간선 정보 읽기
        g.addEdge(u, v);  // 그래프에 간선 추가
    }

    int result = g.scc();  // 강하게 연결된 컴포넌트의 수 계산
    out << result << endl; 

    inp.close(); 
    out.close();

    return 0;
}
