# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

# 다음과 같은 수 분포가 있으면,
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

# 최빈수는 8이 된다.
# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

# [제약 사항]
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.
 
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.


T = int(input())

for test_case in range(1, T + 1):
    test_case_number = int(input())
    num_list = list(map(int, input().split()))
    
    # 점수 카운트 리스트
    num_check = [0] * 101

    # 점수 빈도수 카운트
    for score in num_list:
        num_check[score] += 1

    # 최빈수 여러 개일 경우 가장 큰 점수 선택
    max_index = 0
    max_count = 0
    
    for score in range(101):
        if num_check[score] > max_count or (num_check[score] == max_count and score > max_index):
            max_index = score
            max_count = num_check[score]

    print(f"#{test_case_number} {max_index}")
