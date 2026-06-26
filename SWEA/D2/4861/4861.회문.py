# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. 
# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

# 예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.


# G   O   F   F   A   K   W   F   S   M
# O   Y   E   C   R   S   L   D   L   Q
# U   J   A   J   Q   V   S   Y   Y   C
# J   A   E   Z   N   N   Z   E   A   J //
# W   J   A   K   C   G   S   G   C   F
# Q   K   U   D   G   A   T   D   Q   L
# O   K   G   P   F   P   Y   R   K   Q
# T   D   C   X   B   M   Q   T   I   O
# U   N   A   D   R   P   N   E   T   Z
# Z   A   T   W   D   E   K   D   Q   F


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/4861/sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    # N x N 글자판(문자열 리스트)
    board = [input() for _ in range(N)]
    ans = ""

    # 1. 가로 방향 탐색
    for i in range(N):
        # 길이가 M인 구간 슬라이딩 윈도우처럼 이동
        for j in range(N - M + 1):
            target = board[i][j : j + M]
            if target == target[::-1]:  # 회문 확인
                ans = target
                break
        if ans: break  # 회문 찾으면 탈출

    # 가로에서 못 찾았을 경우에만 세로 방향 탐색
    if not ans:
        for j in range(N):  # 열 고정
            for i in range(N - M + 1):  # 행 시작 위치 이동
                # 세로 문자열 만들기
                target = ""
                for k in range(M):
                    target += board[i + k][j]
                
                if target == target[::-1]:  # 회문 확인
                    ans = target
                    break
            if ans: break

    print(f"#{tc} {ans}")