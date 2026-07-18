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

T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    
    # 격자판 입력받기
    grid = [input().strip() for _ in range(H)]
    
    # 검은색('#')이 존재하는 행과 열의 번호를 저장할 세트
    black_rows = set()
    black_cols = set()
    
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '#':
                black_rows.add(r)
                black_cols.add(c)
    
    # 검은색이 아예 없으면 0, 있으면 둘 중 최솟값
    if not black_rows:
        ans = 0
    else:
        ans = min(len(black_rows), len(black_cols))
        
    print(f"#{test_case} {ans}")