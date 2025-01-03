# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.


# [제약 사항]
# 월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.
# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
# 두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.


# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
# 첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.


# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())


month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, T + 1):
    
    arr = list(map(int, input().split()))
    start_month, start_day, end_month, end_day = arr[0], arr[1], arr[2], arr[3]

    ans = 0

    if start_month == end_month:
        # 같은 달인 경우
        ans = end_day - start_day + 1
    else:
        # 시작 월의 남은 일수 추가
        ans += month_days[start_month] - start_day + 1
        
        # 시작 월, 종료 월 사이의 월의 일수를 모두 더함
        for month in range(start_month + 1, end_month):
            ans += month_days[month]

        # 종료 월의 일수 추가
        ans += end_day

    print(f'#{test_case} {ans}')