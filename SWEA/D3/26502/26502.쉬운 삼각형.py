# 2차원 평면 위에 N개의 서로 다른 점이 있다. 각 점의 x, y 좌표는 정수이다.
# 당신은 이 중 서로 다른 3개의 점을 골라서 삼각형을 만들려고 한다.
# 이 때 삼각형의 한 변은 x축에 평행해야 하고, 다른 한 변은 y축에 평행해야 한다.
 
# 당신이 만들 수 있는 삼각형의 최대 넓이는 얼마인가?
# 넓이에 2를 곱하면 정수가 되니, 최대 넓이에 2를 곱해 출력하라.
# 만들 수 있는 삼각형이 최소 하나 존재한다. 


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다. 
#     -  첫 번째 줄에 점의 수 N이 주어진다. (3 ≤ N ≤ 100)
#     -  이후 N개의 줄에 점의 좌표 xi, yi 가 주어진다. 모든 좌표는 서로 다르고, 좌표는 절댓값이 10000 이하인 정수이다. 


# [출력]
# 각 테스트 케이스 마다 한 줄씩, 문제의 정답을 출력하라.

import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/26502/1_sample_input.txt","r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    
    max_area_2 = 0
    
    # 세 점을 선택하여 직각삼각형 조건 확인
    # p1: 직각이 되는 꼭짓점
    # p2: p1과 y좌표가 같은 점 (가로 변)
    # p3: p1과 x좌표가 같은 점 (세로 변)
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if i == k or j == k: continue
                
                p1, p2, p3 = points[i], points[j], points[k]
                
                # 조건: p1-p2는 x축 평행, p1-p3는 y축 평행
                if p1[1] == p2[1] and p1[0] == p3[0]:
                    # 넓이 * 2 = 밑변 * 높이
                    area_2 = abs(p1[0] - p2[0]) * abs(p1[1] - p3[1])
                    if area_2 > max_area_2:
                        max_area_2 = area_2
                        
    print(f"#{tc} {max_area_2}")