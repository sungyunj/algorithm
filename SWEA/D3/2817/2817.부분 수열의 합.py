# A_1, A_2, ... , A_N의 N개의 자연수가 주어졌을 때, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하는 프로그램을 작성하시오.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 2개의 자연수 N(1 ≤ N ≤ 20)과 K(1 ≤ K ≤ 1000)가 주어진다.
# 두 번째 줄에는 N개의 자연수 수열 A가 주어진다. 
# 수열의 원소인 N개의 자연수는 공백을 사이에 두고 주어지며, 1 이상 100 이하임이 보장된다.


# [출력]
# 각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.

# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/2817/sample_input.txt","r")

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # dp[i]는 합 i를 만들 수 있는 경우의 수
    dp = [0] * (K + 1)
    dp[0] = 1  # 아무것도 선택하지 않았을 때 합 0이 되는 경우 1가지
    
    for num in A:
        # K부터 num까지 거꾸로 확인 (중복 선택 방지)
        for i in range(K, num - 1, -1):
            dp[i] += dp[i - num]
            
    print(f"#{t} {dp[K]}")