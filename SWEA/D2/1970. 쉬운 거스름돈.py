# 우리나라 화폐 ‘원’은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다.

# S마켓에서 사용하는 돈의 종류는 다음과 같다.
# 50,000 원
# 10,000 원
# 5,000 원
# 1,000 원
# 500 원
# 100 원
# 50 원
# 10 원

# S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.

# [예제]

# N이 32850일 경우,
# 50,000 원 : 0개
# 10,000 원 : 3개
# 5,000 원 : 0개
# 1,000 원 : 2개
# 500 원 : 1개
# 100 원 : 3개
# 50 원 : 1개
# 10 원 : 0개

# [제약 사항]
# 1. N은 10이상 1,000,000이하의 정수이다. (10 ≤ N ≤ 1,000,000)
# 2. N의 마지막 자릿수는 항상 0이다. (ex : 32850)

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.

# [출력]
# 각 줄은 '#t'로 시작하고, 다음줄에 각 돈의 종류마다 필요한 개수를 빈칸을 사이에 두고 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())

currency = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):

    N = int(input())  # 거슬러 줄 금액
    result = []  # 각 화폐 단위 저장

    for unit in currency:

        count = N // unit
        result.append(count)
        
        N %= unit  # 남은 금액 계산

    print(f"#{test_case}")
    print(" ".join(map(str, result)))
