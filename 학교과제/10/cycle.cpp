#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

// 방문 확인을 위한 배열
vector<bool> visited;

// 깊이 우선 탐색(DFS) 함수
void dfs(int node, vector<long long>& permute) {
    // 현재 노드를 방문했음으로 표시
    visited[node] = true;
    // 다음 노드는 현재 노드가 가리키는 순열의 위치
    int nextNode = permute[node] - 1;
    // 다음 노드가 아직 방문되지 않았다면, DFS를 계속 진행
    if (!visited[nextNode]) {
        dfs(nextNode, permute);
    }
}

int main() {
    // 입력 파일과 출력 파일 스트림 생성
    ifstream inp("cycle.inp");
    ofstream out("cycle.out");

    long long n; // 테스트 케이스의 수
    inp >> n;

    while (n--) {
        long long n; // 순열의 크기
        inp >> n;

        // 순열을 저장할 벡터
        vector<long long> permute(n);
        // 방문 배열을 false로 초기화하여 방문하지 않음 상태로 만듦
        visited.assign(n, false);

        // 순열 입력 받기
        for (int i = 0; i < n; ++i) {
            inp >> permute[i];
        }

        long long cycleCount = 0; // 순열 사이클의 수를 저장할 변수

        // 모든 노드에 대해 DFS를 실행하여 사이클 찾기
        for (int i = 0; i < n; ++i) {
            // 아직 방문하지 않은 노드라면
            if (!visited[i]) {
                // 해당 노드에서 DFS 시작
                dfs(i, permute);
                // DFS가 완료되면 하나의 사이클이 완성된 것이므로 사이클 수 증가
                cycleCount++;
            }
        }

        // 결과 출력
        out << cycleCount << endl;
    }
    
    // 파일 스트림 닫기
    inp.close();
    out.close();

    return 0;
}
