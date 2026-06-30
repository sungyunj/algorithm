# 그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.

# pic = '4836.1.png'

# 예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
# 2

# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

# color = 1 (빨강), color = 2 (파랑)
 

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/4836/sample_input.txt","r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 1. 10x10 격자판을 0으로 초기화
    grid = [[0] * 10 for _ in range(10)]

    # 보라색 칸의 수를 저장할 변수
    puple_c = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 2. 지정된 영역에 색칠하기 (r1부터 r2까지, c1부터 c2까지)
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                grid[r][c] += color
    
    # 3. 전체 격자를 순회하며 보라색(3)이 된 칸의 개수 세기
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 3:
                puple_c += 1

    print(f"#{tc} {puple_c}")