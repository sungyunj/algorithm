# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

# N = 0.625
# 0.101 (이진수)
# = 1*2^-1 + 0*2^-2 + 1*2^-3
# = 0.5 + 0 + 0.125
# = 0.625

# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.


# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 소수점 아래가 12자리 이내인 N이 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/5186/sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    
    result = ""
    cnt = 0  # 자릿수를 세기 위한 변수
    
    # N이 0이 될 때까지 반복
    while N > 0:
        N *= 2
        cnt += 1
        
        # 13자리 이상 필요해지면 바로 overflow 처리 후 종료
        if cnt >= 13:
            result = "overflow"
            break
            
        if N >= 1:
            result += "1"
            N -= 1  # 정수 부분 1 빼줌
        else:
            result += "0"
            
    print(f"#{tc} {result}")