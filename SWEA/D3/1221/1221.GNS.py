# 숫자 체계가 우리와 다른 어느 행성이 있다. 
# 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.


# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
# 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백 문자 후 테스트 케이스의 길이가 주어진다.
# 테스트 케이스의 길이란, 문자열의 글자수가 아닌 단어의 갯수를 말한다.
# 그 다음 줄부터 바로 테스트 케이스가 주어진다. 
# 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.


# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.



# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/1221/GNS_test_input.txt", "r")

num = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}

T = int(input())

for _ in range(T):
    # 테스트 케이스 번호와 길이를 입력 (예: #1 7041)
    tc_info = input().split()
    tc_num = tc_info[0]
    n = int(tc_info[1])
    
    # 데이터 리스트 입력
    data = input().split()
    
    # num의 value를 기준으로 정렬
    data.sort(key=lambda x: num[x])
    
    # 결과 출력
    print(tc_num)
    print(*(data))

