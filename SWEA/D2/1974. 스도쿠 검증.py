# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

# [제약 사항]
# 1. 퍼즐은 모두 숫자로 채워진 상태로 주어진다.
# 2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9 이하의 정수이다.


# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스는 9 x 9 크기의 퍼즐의 데이터이다.


# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    def checkSudoku():
        # 조건1: 3x3 박스 검사
        for r in range(0, 9, 3):  # 3칸씩 건너뜀
            for c in range(0, 9, 3):
                numbers_box = []
                for i in range(3):
                    for j in range(3):
                        numbers_box.append(arr[r + i][c + j])
                if sorted(numbers_box) != list(range(1, 10)):  # 1~9 포함 확인
                    return 0

        # 조건2: 가로와 세로 검사
        for i in range(9):
            row = []
            column = []
            for j in range(9):
                row.append(arr[i][j])      # i번째 행
                column.append(arr[j][i])  # i번째 열
            if sorted(row) != list(range(1, 10)) or sorted(column) != list(range(1, 10)):
                return 0

        return 1

    print(f"#{test_case} {checkSudoku()}")
