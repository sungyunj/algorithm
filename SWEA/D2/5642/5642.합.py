# N개의 정수가 입력으로 주어진다.
# 이때 연속하여 몇 개의 정수를 골라 합을 구할 수 있다.
# 예를 들어, 1 3 -8 18 -8 이 있다고 하자.
# 그럼 2번부터 4번까지의 수를 골라 합을 구하면, 3+(-8)+18 = 13이다. 
# 이렇게 연속해서 정수를 골라 합을 구할 때, 그 합의 최대가 몇인지 구하는 프로그램을 작성하세요.


# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)
# 각 테스트 케이스 첫째 줄에 숫자 N이 주어진다. (3 ≤ N ≤ 100,000)
# 둘째 줄에는 절대값이 1000이하의 정수 N개가 공백을 사이에 두고 입력된다.


# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, 연속된 정수의 합의 최대값을 출력하시오.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/5642/sample_input.txt","r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int,input().split()))
    # 각 단계에서 이전까지의 합에 현재 숫자를 더하는 것이 이득인가
    # 아니면 여기서부터 새로 시작하는 것이 이득인가를 결정
    max_sum = A[0]
    cur_sum = A[0]

    for i in range(1, N):
        # (이전까지의 합 + 현재 값) vs (현재 값) 중 큰 것을 선택
        # current_sum + nums[i]가 nums[i]보다 작다면 
        # 앞선 합이 마이너스라는 뜻. 새로 시작하는 게 이득
        cur_sum = max(cur_sum + A[i], A[i])

        if cur_sum > max_sum:
            max_sum = cur_sum
    
    print(f"#{tc} {max_sum}")