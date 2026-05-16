# 아래 그림과 같은 미로가 있다. 
# 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
# 아래의 예시에서는 도달 가능하다.
 
# pic1 = "1227.1.png"

# 아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.
 
# pic1 = "1227.2.png"

# 위의 예시는 공간상의 이유로 100x100이 아닌 16x16으로 주어졌음에 유의한다.


# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트 케이스가 주어진다.
# 테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).


# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D4/1227/input.txt","r")
from collections import deque

def bfs(sy, sx):
    # 1. 큐 생성 및 시작점 삽입
    queue = deque([(sy, sx)])
    # 시작점 방문 처리 (벽으로 만듦)
    maze[sy][sx] = 1
    
    # 4방향 나침반
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    # 2. 큐가 빌 때까지 반복
    while queue:
        y, x = queue.popleft() # 가장 먼저 들어온 좌표 꺼내기
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 미로 범위(100x100)
            if 0 <= ny < 100 and 0 <= nx < 100:
                # 도착점 
                if maze[ny][nx] == 3:
                    return 1
                
                # 길(0)이라면 큐에 추가, 방문 처리
                if maze[ny][nx] == 0:
                    maze[ny][nx] = 1 # 방문한 길은 벽으로 변경하여 중복 방지
                    queue.append((ny, nx))
                    
    return 0 # 도착점을 찾지 못함

# 10개의 테스트 케이스 처리
for _ in range(10):
    num = input().strip()
    # 100줄의 미로 데이터를 읽어옴
    maze = [list(map(int, input().strip())) for _ in range(100)]
    
    # 시작점 (1, 1)에서 탐색 시작
    result = bfs(1, 1)
    print(f"#{num} {result}")