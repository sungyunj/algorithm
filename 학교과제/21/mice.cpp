#include <iostream>
#include <fstream>
#include <utility>
#include <deque>
#include <cstring>
#include <vector>

using namespace std;

typedef pair<int, int> Point;

// 세 점의 방향성을 판별하는 ccw 함수 정의
int ccw(long long x1, long long y1, long long x2, long long y2, long long x3, long long y3) {
    long long res = (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1);
    if (res > 0) return 1;   // 반시계 방향
    if (res < 0) return -1;  // 시계 방향
    return 0;                // 일직선
}

int main() {
    ifstream inp("mice.inp");  // 입력 파일 열기
    ofstream out("mice.out"); // 출력 파일 열기

    int T;
    inp >> T; // 테스트 케이스 수 입력 받기

    while (T--) {
        int n, k, h, m, x, y;
        inp >> n >> k >> h >> m; // 각 테스트 케이스에 대한 입력 값 받기

        vector<Point> house(n), hole(h), mouse(m);
        for (int i = 0; i < n; i++) {
            inp >> x >> y;
            house[i] = Point(x, y);
        }
        for (int i = 0; i < h; i++) {
            inp >> x >> y;
            hole[i] = Point(x, y);
        }
        for (int i = 0; i < m; i++) {
            inp >> x >> y;
            mouse[i] = Point(x, y);
        }

        vector<vector<int> > graph(h + m + 2, vector<int>(h + m + 2, 0)); // 그래프 초기화
        for (int i = 1; i <= h; i++) {
            graph[0][i] = k;  // 쥐구멍의 용량 설정
        }
        for (int i = h + 1; i <= h + m; i++) {
            graph[i][h + m + 1] = 1; // 쥐의 용량 설정
        }
        for (int i = 0; i < h; i++) {
            int h_x = hole[i].first;
            int h_y = hole[i].second;
            for (int j = 0; j < m; j++) {
                int m_x = mouse[j].first;
                int m_y = mouse[j].second;
                bool isValid = true;

                // 집의 모든 변에 대해 체크
                for (int p = 0; p < n; p++) {
                    int x1 = house[p].first;
                    int y1 = house[p].second;
                    int x2 = house[(p + 1) % n].first;
                    int y2 = house[(p + 1) % n].second;
                    
                    if (ccw(x1, y1, h_x, h_y, x2, y2) == 0) continue;
                    if (ccw(x1, y1, x2, y2, h_x, h_y) * ccw(x1, y1, x2, y2, m_x, m_y) > 0) continue;
                    if (ccw(h_x, h_y, m_x, m_y, x1, y1) * ccw(h_x, h_y, m_x, m_y, x2, y2) > 0) continue;
                    isValid = false;
                    break;
                }
                if (isValid) {
                    graph[i + 1][h + j + 1] = 1; // 경로 추가
                }
            }
        }
        int resultCount = 0;
        while (true) {
            vector<int> prevNode(h + m + 2, -1);
            deque<Point> queue;
            queue.push_back(Point(0, k + 1));

            // 너비 우선 탐색 (BFS)을 통해 증가 경로 찾기
            while (!queue.empty() && prevNode[h + m + 1] == -1) {
                int currentNode = queue.front().first;
                int minRest = queue.front().second;
                queue.pop_front();

                for (int nextNode = 1; nextNode <= h + m + 1; nextNode++) {
                    if (prevNode[nextNode] == -1 && graph[currentNode][nextNode]) {
                        prevNode[nextNode] = currentNode;
                        queue.push_back(Point(nextNode, min(minRest, graph[currentNode][nextNode])));
                    }
                }
            }
            if (prevNode[h + m + 1] == -1) break; // 증가 경로 없음

            int flow = k + 1;  // 최소 잔여 용량 찾기
            for (int v = h + m + 1; v != 0; v = prevNode[v]) {
                int u = prevNode[v];
                flow = min(flow, graph[u][v]);
            }

            // 역방향 간선 갱신
            for (int v = h + m + 1; v != 0; v = prevNode[v]) {
                int u = prevNode[v];
                graph[u][v] -= flow;
                graph[v][u] += flow;
            }
            resultCount += flow; // 흐름 추가
        }

        if (resultCount == m) out << "Possible\n"; // 모든 쥐가 숨을 수 있는 경우
        else out << "Impossible\n"; // 그렇지 않은 경우
    }
}
