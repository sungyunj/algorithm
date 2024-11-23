# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

# [제약사항]

# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스에는 N이 주어진다.


# [출력]

# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def snailArray(n):
    snail = [[0] * n for _ in range(n)]
    num = 1
    x, y = 0, 0  # 초기 위치
    dx, dy = 0, 1  # 초기 이동 방향 (오른쪽)

    for _ in range(n * n):
        snail[x][y] = num
        num += 1

        # 다음 위치 계산
        nx, ny = x + dx, y + dy

        # 범위를 벗어나거나 이미 숫자가 있는 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or snail[nx][ny] != 0:
            dx, dy = dy, -dx  # 오른쪽 → 아래 → 왼쪽 → 위쪽 순으로 방향 변경
            nx, ny = x + dx, y + dy

        x, y = nx, ny

    return snail


T = int(input())
results = []

for t in range(1, T + 1):
    N = int(input())
    snail_array = snailArray(N)
    results.append((t, snail_array))

for t, snail_array in results:
    print(f"#{t}")
    for row in snail_array:
        print(" ".join(map(str, row)))
