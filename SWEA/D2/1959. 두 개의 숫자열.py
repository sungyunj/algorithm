# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.
# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.

# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

# [제약 사항]
# N 과 M은 3 이상 20 이하이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 두 번째 줄에는 Ai,
# 세 번째 줄에는 Bj 가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A와 B의 길이에 따라 스왑. 항상 A가 짧고 B가 길게
    if N > M:
        A, B = B, A
        N, M = M, N

    max_sum = -float('inf')

    # A를 B의 모든 가능한 위치에 맞춰 계산
    for i in range(M - N + 1):
        temp_sum = 0
        for j in range(N):
            temp_sum += A[j] * B[i + j]
        max_sum = max(max_sum, temp_sum)

    print(f"#{t} {max_sum}")
