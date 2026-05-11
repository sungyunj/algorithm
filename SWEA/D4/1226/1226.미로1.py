# 아래 그림과 같은 미로가 있다. 
# 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
# 가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

# 아래의 예시에서는 도달 가능하다.

pic1 = "1226.1.png"

# 아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.

pic2 = "1226.2.png"

# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트케이스가 주어진다.
# 테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 
# (1 - 가능함, 0 - 가능하지 않음).



# import sys
# sys.stdin = open("input.txt","r")
'''
import sys
import os

파일 경로를 못 찾는 에러 방지를 위한 안전한 경로 설정
file_path = os.path.join(os.path.dirname(__file__), "input.txt")
sys.stdin = open(file_path, "r")
'''

# # 1. 재귀 깊이 제한 늘리기 (미로 탐색 필수)
# sys.setrecursionlimit(10**6)

def dfs(y, x):
    # 도착 지점(3)에 도달하면 성공(1) 반환
    if maze[y][x] == 3:
        return 1
    
    # 현재 위치를 방문 처리 (벽 1로 변경)
    maze[y][x] = 1
    
    # 4방향 나침반 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        # 미로 범위(16x16) 안에 있고, 벽(1)이 아니라면 이동 가능
        if 0 <= ny < 16 and 0 <= nx < 16:
            if maze[ny][nx] == 0 or maze[ny][nx] == 3:
                # 다음 칸에서 결과를 찾았다면(1) 나도 성공 보고
                if dfs(ny, nx) == 1:
                    return 1
    
    # 4방향 다 가봤는데 도착점이 없으면 실패(0)
    return 0

# 총 10개의 테스트 케이스
for _ in range(10):
    # 테스트 케이스 번호 읽기
    tc_num = input().strip()
        
    # 16줄의 미로 데이터를 2차원 리스트로 읽기
    # 한 줄의 문자열을 하나씩 정수로 쪼개기
    maze = [list(map(int, input().strip())) for _ in range(16)]
        
    # (1, 1)에서 시작해서 결과 확인
    result = dfs(1, 1)
        
    # 출력 형식: #번호 결과
    print(f"#{tc_num} {result}")

# "첫 줄에 테스트 케이스의 개수 T가 주어진다" 라고 할 때 밑에 출력 코드
'''
# T = int(input()) 이 있는 경우
T = int(input()) 

for test_case in range(1, T + 1):
    # 만약 문제에서 각 케이스마다 번호를 또 준다면?
    # tc_num = input() 
    
    maze = [list(map(int, input().strip())) for _ in range(16)]
    
    result = dfs(1, 1)
    print(f"#{test_case} {result}")
'''