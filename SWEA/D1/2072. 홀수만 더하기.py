# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.


# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())

results = []

for i in range(1, T+1):
    
    odd_sum = 0
    a = list(map(int,input().split()))

    for j in range(len(a)):

        if a[j] % 2 == 1:
            odd_sum += a[j]
    
    results.append(f"#{i} {odd_sum}")

for result in results:
    print(result)