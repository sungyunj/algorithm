# NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
# 주어진 미로 밖으로는 나갈 수 없다.

# 다음은 5x5 미로의 예이다.

# 13101
# 10101
# 10101
# 10101
# 10021

# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.



from collections import deque
# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/4875/sample_input.txt", "r")

def bfs(sy, sx):
    queue = deque([(sy, sx)])
    
    # 시작점 방문 처리 (벽으로 변경)
    maze[sy][sx] = 1

    # 상, 하, 좌, 우 4방향 이동을 위한 델타값 (Y, X축 기준)
    # dy는 세로(행), dx는 가로(열)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 미로 범위 내에 있는 경우
            if 0 <= ny < N and 0 <= nx < N:
                # 목적지(3)를 찾았다면 성공(1) 반환
                if maze[ny][nx] == 3:
                    return 1
                
                # 갈 수 있는 통로(0)라면 큐에 넣고 방문 처리(1)
                if maze[ny][nx] == 0:
                    queue.append((ny, nx))
                    maze[ny][nx] = 1 
                    
    # 목적지에 도달하지 못하고 큐가 비었다면 0 반환
    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    
    # 출발점(2) 좌표 찾기
    sy, sx = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j  # i가 세로(y), j가 가로(x)
                break
        if sy != -1:
            break

    rlt = bfs(sy, sx)
    print(f"#{tc} {rlt}")