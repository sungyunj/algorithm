# N^2개의 방이 N×N형태로 늘어서 있다.
# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N^2 이하의 수 A_i, _j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 10^3)이 주어진다.
# 다음 N개의 줄에는 i번째 줄에는 N개의 정수 A_i, 1, … , A_i, N (1 ≤ A_i, _j ≤ N^2) 이 공백 하나로 구분되어 주어진다.
# A_i, _j는 모두 서로 다른 수이다.


# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.
# 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


# [예제 풀이]
# 첫 번째 테스트 케이스는 1 또는 3이 적힌 곳에 있어야 한다.
# 두 번째 테스트 케이스는 3 또는 6이 적힌 곳에 있어야 한다.


# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D4/1861/input.txt","r")
# 입력 속도 최적화
# input = sys.stdin.readline

# 상하좌우 방향 설정
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
    
    max_dist = 0
    start_num = 0
    
    # 각 숫자가 어느 좌표(y, c)에 있는지 저장 (속도 향상)
    pos = [0] * (N*N + 1)
    for y in range(N):
        for x in range(N):
            pos[maze[y][x]] = (y, x)
            
    # 연속된 숫자가 있는지 체크 리스트
    # checked[i] = 1 이면 i번 방에서 i+1번 방으로 갈 수 있다
    checked = [0] * (N*N + 1)
    
    for num in range(1, N*N):
        y, x = pos[num]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 상하좌우에 나보다 정확히 1 큰 숫자가 있다
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] == num + 1:
                    checked[num] = 1
                    break
    
    # 이제 checked 배열에서 가장 길게 연속된 1의 구간을 찾으면 끝
    curr_dist = 1
    for num in range(N*N, 0, -1):
        if checked[num - 1]:
            curr_dist += 1
        else:
            # 더 길거나, 길이는 같은데 숫자가 작으면 갱신
            if curr_dist >= max_dist:
                max_dist = curr_dist
                start_num = num
            curr_dist = 1 # 초기화
            
    print(f"#{tc} {start_num} {max_dist}")