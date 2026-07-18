# H x W 크기의 격자판이 있다. 처음에 모든 격자는 흰색으로 칠해져 있다. 당신은 아래와 연산을 0회 이상 사용하여 일부 격자를 검은색으로 칠하였다.
#   -  격자판의 행 하나 또는 열 하나를 고른다.
#   -  고른 행 또는 열에 있는 모든 칸을 검은색으로 칠한다. 이미 검은색인 칸을 한 번 더 검은색으로 칠하면 여전히 검은색을 유지한다.
# 현재 격자판의 상태가 주어질 때, 이러한 상태를 만들기 위해 최소 몇 번의 연산을 사용해야 하는지 구하는 프로그램을 작성하라.
 

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 아래와 같은 구성으로 이루어진다.
#   -  첫 번째 줄에는 격자판의 행 수 H와 열 수 W(1 ≤ H, W ≤ 50)이 주어진다.
#   -  다음 H개의 줄에는 격자판의 색을 나타내는 W개의 문자가 주어진다. i번째 줄의 j번째 문자는, 격자판의 i행 j열이 검은색이면 “#”, 흰색이면 “.”이다. 문제에서 제시한 연산만을 사용하여 만들 수 있는 상태만 주어진다.


# [출력]
# 각 테스트 케이스마다, 주어진 격자판 상태를 만들기 위해 필요한 최소 연산 횟수를 한 줄에 하나씩 출력한다.



import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/25469/1_sample_input.txt","r")

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())

    # graph[i] : i번 행과 연결된(검은색인) 열들
    graph = [[] for _ in range(H)]

    for i in range(H):
        s = input().strip()
        for j, c in enumerate(s):
            if c == '#':
                graph[i].append(j)

    # match[j] = j번 열과 매칭된 행 번호
    # -1이면 아직 매칭되지 않음
    match = [-1] * W

    def dfs(v):
        for nxt in graph[v]:
            if visited[nxt]:
                continue
            visited[nxt] = True

            # 비어있는 열이거나,
            # 기존 매칭을 다른 곳으로 옮길 수 있으면 매칭 성공
            if match[nxt] == -1 or dfs(match[nxt]):
                match[nxt] = v
                return True

        return False

    ans = 0

    # 모든 행에서 증가 경로 탐색
    for i in range(H):
        visited = [False] * W
        if dfs(i):
            ans += 1

    # 최대 매칭 = 최소 정점 커버 = 최소 연산 횟수
    print(ans)