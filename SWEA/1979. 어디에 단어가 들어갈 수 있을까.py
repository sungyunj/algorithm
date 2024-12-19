# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# [제약 사항]
# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())  # 테스트 케이스 수 입력

for test_case in range(1, T + 1):
    # N, K 입력
    N, K = map(int, input().split())
    
    # 퍼즐 보드 입력
    board = [input().split() for _ in range(N)]
    
    match_string = '1' * K  # 찾으려는 연속된 1의 문자열

    # 행 순회
    row_cnt = 0
    for row in board:
        str_row = "".join(row).split("0")
        row_cnt += str_row.count(match_string)

    # 열 순회
    col_cnt = 0
    for col in zip(*board):  # 열을 추출
        str_col = "".join(col).split("0")
        col_cnt += str_col.count(match_string)

    # 결과 출력
    print(f"#{test_case} {row_cnt + col_cnt}")
