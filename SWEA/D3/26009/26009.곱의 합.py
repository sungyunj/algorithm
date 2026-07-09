# 세 정수 a,b,c 가 주어졌을 때, pic1을 998244353 으로 나눈 나머지를 출력하라. 

# pic1 = '26009.1.png'

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다. 
# -  첫 번째 줄에 세 정수 a, b, c 가 주어진다. (1 ≤ a, b, c ≤ 10^9)


# [출력]
# 각 테스트 케이스 마다 한 줄씩, 정답을 출력하라.



import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/26009/1_sample_input.txt","r")

def solve():
    tc = int(input())
    
    MOD = 998244353
    
    # 1부터 N까지의 합을 MOD 연산하며 구하는 함수
    def get_sum(n):
        # n과 n+1 중 하나는 반드시 짝수이므로, 먼저 2로 나누어 소수점 발생을 방지
        if n % 2 == 0:
            term1 = (n // 2) % MOD
            term2 = (n + 1) % MOD
        else:
            term1 = n % MOD
            term2 = ((n + 1) // 2) % MOD
        return (term1 * term2) % MOD

    for _ in range(tc):
        a, b, c = map(int, input().split())
        
        # 각각의 합을 구함
        sum_a = get_sum(a)
        sum_b = get_sum(b)
        sum_c = get_sum(c)
        
        # 최종 곱의 합 구하기 (중간중간 MOD 연산)
        ans = (sum_a * sum_b) % MOD
        ans = (ans * sum_c) % MOD

        print(ans)

if __name__ == '__main__':
    solve()