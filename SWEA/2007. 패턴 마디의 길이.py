# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.


# [제약 사항]

# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


def find_pattern_length(s):
    
    for length in range(1, 11):
        pattern = s[:length] # 첫 번째 마디를 추출
        repeated = pattern * (len(s) // length) # 마디 문자열 길이만큼

        if repeated == s[:len(repeated)]:
            return length
        
    return len(s)


T = int(input())
results = []

for t in range(1, T + 1):
    test_case = input().strip()
    pattern_length = find_pattern_length(test_case)
    results.append(f"#{t} {pattern_length}")

for result in results:
    print(result)
