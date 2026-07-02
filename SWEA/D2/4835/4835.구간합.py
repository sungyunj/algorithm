# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
 
# 다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.

#     v   1   2   3   4   5

#     v   1   2   3   4   5

# 이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
 
# v   1   2   3   4   5

# 이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
# 답은 12와 6의 차인 6을 출력한다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/4835/sample_input.txt","r")

T = int(input())

for tc in range(1, T + 1):
    # N(정수의 개수), M(구간의 크기)
    N, M = map(int, input().split())
    
    # N개의 정수 배열 입력
    arr = list(map(int, input().split()))
    
    # 최댓값과 최솟값을 저장할 변수 초기화
    max_sum = float('-inf')
    min_sum = float('inf')
    
    # 구간합 구하기
    for i in range(N - M + 1):
        # i부터 i+M 전까지의 부분 배열의 합 계산
        current_sum = sum(arr[i:i+M])
        
        # 최댓값과 최솟값 갱신
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum

    result = max_sum - min_sum
    print(f"#{tc} {result}")