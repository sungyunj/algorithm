# 두 자연수 S와 P가 주어질 때, N + M = S, N * M = P 인 두 자연수 (N, M) 이 존재하면 “Yes”, 존재하지 않으면 “No” 를 출력하라. 


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다. 
# -  첫 번째 줄에는 두 정수 S, P 가 주어진다. (1 ≤ S, P ≤ 10^12)


# [출력]
# 각 테스트 케이스 마다 한 줄씩, 정답을 출력하라.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/25837/1_sample_input.txt","r")


def solve():
    try:
        tc_input = input()
        if not tc_input:
            return
        TC = int(tc_input)
    except EOFError:
        return

    for _ in range(TC):
        S, P = map(int, input().split())
        
        # 1. 판별식 D = S^2 - 4P
        D = S * S - 4 * P
        
        # 음수면 실근이 없으므로 No
        if D < 0:
            print("No")
            continue
        
        # 2. 이분 탐색으로 D의 정수 제곱근 구하기
        low, high = 0, D
        sqrt_D = 0
        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid
            if mid_sq == D:
                sqrt_D = mid
                break
            elif mid_sq < D:
                sqrt_D = mid  # 일단 가장 가까운 값 저장
                low = mid + 1
            else:
                high = mid - 1
        
        # 3. 완전제곱수인지 판별하고 조건 체크
        if sqrt_D * sqrt_D == D:
            # S와 sqrt_D의 합이 짝수여야 분자가 2로 나누어 떨어집니다.
            if (S + sqrt_D) % 2 == 0:
                # 두 자연수 N, M 계산
                N = (S + sqrt_D) // 2
                M = (S - sqrt_D) // 2
                
                # 둘 다 자연수(1 이상)인지 확인
                if N > 0 and M > 0:
                    print("Yes")
                    continue     
        print("No")

solve()