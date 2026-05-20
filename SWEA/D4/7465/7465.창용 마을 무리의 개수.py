# [제한 사항]
# 시간  | 10개 테스트케이스를 합쳐서 C++ 의 경우 1초 / Java 의 경우 2초 / Python 의 경우 2초

# 메모리 | 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

 

# 창용 마을에는 N명의 사람이 살고 있다.
# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는
# 두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
# 이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.
# 같은 관계는 반복해서 주어지지 않는다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 무리의 개수를 출력한다.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D4/7465/s_input.txt","r")

# 1. 전체 테스트 케이스 개수 입력
T = int(input())

for tc in range(1, T + 1):
    # 2. 각 케이스의 인원(N)과 관계 수(M) 입력
    N, M = map(int, input().split())
    
    # 3. 그래프(인접 리스트) 초기화
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # 4. 방문 여부 체크 리스트
    visited = [False] * (N + 1)
    count = 0
    
    # 5. 1번 사람부터 N번 사람까지 확인
    for i in range(1, N + 1):
        if not visited[i]:
            # 새로운 무리 발견! 카운트 증가
            count += 1
            
            # DFS: 이 사람과 연결된 모든 사람을 방문 처리
            stack = [i]
            visited[i] = True
            
            while stack:
                curr = stack.pop()
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
                        
    print(f"#{tc} {count}")