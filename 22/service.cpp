#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

const int maxTeam = 105;
const int maxNode = 2 + maxTeam * 50 + maxTeam;
const int maxValue = 1e9;

int capacity[maxNode][maxNode], flowEdge[maxNode][maxNode];
vector<int> graphEdge[maxNode];

bool bfs(int startNode, int endNode, vector<int>& parent) {
    fill(parent.begin(), parent.end(), -1);
    queue<int> q;
    q.push(startNode);
    parent[startNode] = startNode;
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        for (int next : graphEdge[current]) {
            if (capacity[current][next] - flowEdge[current][next] > 0 && parent[next] == -1) {
                parent[next] = current;
                q.push(next);
                if (next == endNode) {
                    return true;
                }
            }
        }
    }
    return false;
}

int maxFlow(int startNode, int endNode) {
    memset(flowEdge, 0, sizeof(flowEdge));
    vector<int> parent(maxNode);
    int result = 0;
    
    while (bfs(startNode, endNode, parent)) {
        int flowLimit = maxValue;
        for (int v = endNode; v != startNode; v = parent[v]) {
            int u = parent[v];
            flowLimit = min(flowLimit, capacity[u][v] - flowEdge[u][v]);
        }
        for (int v = endNode; v != startNode; v = parent[v]) {
            int u = parent[v];
            flowEdge[u][v] += flowLimit;
            flowEdge[v][u] -= flowLimit;
        }
        result += flowLimit;
    }
    return result;
}

int main() {
    ifstream inp("service.inp");
    ofstream out("service.out");
    
    int T;
    inp >> T;
    
    while (T--) {
        int N, P, M;
        inp >> N >> P >> M;
        
        vector<int> area(P+1, 0);
        for (int i = 1; i <= P; i++) {
            inp >> area[i];
        }
        
        int totalarea = 0;
        for (int i = 1; i <= P; i++) {
            totalarea += area[i];
            }
        
        int startNode = 0, endNode = 1 + N + totalarea + 1;
        for (int i = 0; i < maxNode; i++) {
            graphEdge[i].clear();
            for (int j = 0; j < maxNode; j++) capacity[i][j] = 0;
        }
        
        int areaStart = 1 + N;
        int currentArea = areaStart;
        
        for (int i = 1; i <= N; i++) {
            graphEdge[startNode].push_back(i);
            graphEdge[i].push_back(startNode);
            capacity[startNode][i] = M;
        }
        
        for (int i = 1; i <= N; i++) {

            int t;
            inp >> t;
            while (t--) {
                int j, k;
                inp >> j >> k;
                int areaNode = areaStart;
                for (int p = 1; p < j; p++) areaNode += area[p];
                areaNode += k - 1;
                
                graphEdge[i].push_back(areaNode);
                graphEdge[areaNode].push_back(i);
                capacity[i][areaNode] = 1;
            }
        }
        
        for (int i = 0; i < totalarea; i++) {
            graphEdge[currentArea + i].push_back(endNode);
            graphEdge[endNode].push_back(currentArea + i);
            capacity[currentArea + i][endNode] = 1;
        }
        
        int max_flow = maxFlow(startNode, endNode);

        out << (max_flow == totalarea ? 1 : 0) << '\n';
    }
    
    return 0;
}