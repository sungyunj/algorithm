# 아래 그림과 같은 미로가 있다. 
# 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
# 최단 거리(몇 칸 만에 갔는지)도 계산
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


# 최단 거리 수만 계산
'''
import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D4/1227/input.txt","r")
from collections import deque

def bfs(sy, sx):
    # 1. 큐에 (y, x, 현재까지의 거리)를 넣기
    # 처음 시작점은 거리가 0(또는 1)
    queue = deque([(sy, sx, 0)])
    maze[sy][sx] = 1 # 방문 처리
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:
        # 2. 현재 위치와 거리(d)를 꺼냄
        y, x, d = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < 100 and 0 <= nx < 100:
                # 3. 도착점 발견 시, 현재 거리 + 1을 반환
                if maze[ny][nx] == 3:
                    return d + 1
                
                if maze[ny][nx] == 0:
                    maze[ny][nx] = 1 
                    # 4. 다음 칸으로 이동할 때 거리를 1 증가시켜서 큐에 넣기
                    queue.append((ny, nx, d + 1))
                    
    return -1 # 길을 못 찾은 경우

for _ in range(10):
    num = input().strip()
    maze = [list(map(int, input().strip())) for _ in range(100)]
    result = bfs(1, 1)

    print(f"#{num} {result}")
'''


#도착 가능 및 최단 거리 계산

import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D4/1227/input.txt","r")
from collections import deque

def bfs(sy, sx):
    # 큐에 (y, x, 현재 거리) 저장
    queue = deque([(sy, sx, 0)])
    maze[sy][sx] = 1 # 방문 처리
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:
        y, x, d = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < 100 and 0 <= nx < 100:
                # 도착점(3) 발견
                if maze[ny][nx] == 3:
                    # (성공여부 1, 최단거리 d+1) 두 개 반환
                    return 1, d + 1
                
                if maze[ny][nx] == 0:
                    maze[ny][nx] = 1 
                    queue.append((ny, nx, d + 1))
                    
    # 다 돌았는데 못 찾았다
    # (성공여부 0, 거리는 없으니까 -1) 반환
    return 0, -1


for _ in range(10):
    num = input().strip()
    maze = [list(map(int, input().strip())) for _ in range(100)]
    
    # 두 개의 변수로 각각 받기
    is_possible, shortest_dist = bfs(1, 1)
    
    if is_possible:
        print(f"#{num} {is_possible} {shortest_dist}")
    else:
        print(f"#{num} {is_possible} {shortest_dist}")