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
