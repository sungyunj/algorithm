# 자연수 N와 R가 주어진다. 
# 이 때의 N combination R의 값을 1234567891로 나눈 나머지를  출력하세요.
# 예를들면 N이 4, R이 2라면 4 combination 2는 (4 * 3) / (2 * 1) = 6이 된다.


# [입력]
# 첫 줄에 테스트케이스의 개수 T가 주어진다. (1 ≤ T ≤ 20)
# 각 케이스의 첫 줄에 정수 N, R이 주어진다. (1 ≤ N ≤ 1000000, 0 ≤ R ≤ N)
 

# [출력]
# 각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(TC) “를 출력하고, N combination R을 1234567891로 나눈 나머지를 출력하시오.



# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/5607/sample_input.txt","r")

# 팩토리얼 배열 미리 만들기 (최대 범위 1,000,000)
# 테스트 케이스 밖에서 한 번만 계산해야 시간 초과가 나지 않음.
MOD = 1234567891
fact = [1] * 1000001
for i in range(2, 1000001):
    fact[i] = (fact[i-1] * i) % MOD

T = int(input())

for tc in range(1, T + 1):
    N, R = map(int, input().split())

    # 조합 공식: N! / (R! * (N-R)!)
    # 분자: N!
    top = fact[N]
    # 분모: R! * (N-R)!
    bottom = (fact[R] * fact[N-R]) % MOD

    # 4. 페르마의 소정리 적용
    # 나누기 bottom 대신, bottom^(MOD-2)를 곱함.
    # pow(a, b, m)은 (a**b) % m 을 아주 빠르게 계산함.
    inv_bottom = pow(bottom, MOD - 2, MOD)

    ans = (top * inv_bottom) % MOD
    print(f"#{tc} {ans}")