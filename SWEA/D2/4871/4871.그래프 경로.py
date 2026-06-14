# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.

pic1 = '4871.png'

# 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
# E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



def dfs(current, target):
    # 현재 노드가 목적지라면 경로가 존재하는 것이므로 1 반환
    if current == target:
        return 1
    
    # 현재 노드 방문 처리
    visited[current] = True
    
    # 현재 노드와 연결된 다음 노드들을 확인
    for next_node in graph[current]:
        if not visited[next_node]: # 아직 방문하지 않은 노드라면
            # 재귀적으로 탐색을 이어감
            if dfs(next_node, target) == 1:
                return 1 # 목적지를 찾았다면 즉시 1을 리턴하며 탈출
                
    return 0 # 모든 연결된 노드를 방문해도 목적지를 못 찾았다면 0 반환


T = int(input()) # 테스트 케이스 개수 입력

for tc in range(1, T + 1):
    # V: 노드 개수, E: 간선 개수
    V, E = map(int, input().split())
    
    # 인접 리스트 초기화 (노드 번호가 1부터 시작하므로 V+1 크기로 생성)
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    
    # 간선 정보 입력 받기
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v) # 방향성 그래프 (u -> v)
        
    # S: 출발 노드, G: 도착 노드
    S, G = map(int, input().split())
    
    # DFS 탐색 시작
    result = dfs(S, G)
    
    print(f"#{tc} {result}")