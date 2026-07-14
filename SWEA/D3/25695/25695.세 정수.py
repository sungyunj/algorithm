# pic1 = '25695.1.png'

# 세 자연수 X, Y, Z가 있다.
# X = max(A, B), Y = max(B, C), Z = max(C, A)를 만족시키는 세 정수 A, B, C가 존재하는지 판단하고, 존재한다면 그 중 한 순서쌍을 출력하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 세 개의 정수 X, Y, Z가 주어진다. 각 정수는 1 이상 109 이하이다.


# [출력]
# 각 테스트 케이스마다, 
#     -  조건을 만족하는 A, B, C가 존재하지 않는다면 “-1 -1 -1”을 출력한다.
#     -  조건을 만족하는 A, B, C가 존재한다면 그 중 한 가지를 공백 하나씩을 사이로 두고 출력한다.



import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/25695/1_sample_input.txt","r")

T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    
    # 크기 순으로 정렬 (가장 큰 값이 2개 이상 있는지 확인)
    arr = sorted([X, Y, Z])
    
    # 가장 큰 두 값이 서로 다르면 (최댓값이 1개뿐이면) 불가능
    if arr[1] != arr[2]:
        print("-1 -1 -1")
    else:
        # arr[2]가 가장 큰 값(M), arr[0]이 가장 작은 값(m).
            # A, B, C를 적절히 매칭. 
            # X = max(A, B), Y = max(B, C), Z = max(C, A)
            
            # 한 가지 확실한 해는 세 수 중 두 개를 최댓값 M으로 두고, 하나를 m으로 둠.
            # 어떤 변수가 어떤 값을 가질지는 X, Y, Z의 위치에 맞춰 지정.
            
            # 예시:
            # X가 큰 값들 중 하나, Y가 큰 값들 중 하나라면 B를 M으로 두는 식.
            # 가장 깔끔한 방법은 X, Y, Z의 값에 따라 분기처리하거나 아래와 같이 구성할 수 있음.

        # X, Y, Z 조건에 맞춰 A, B, C 조합 찾기
        if X == Y and X >= Z:
            A = Z
            B = X
            C = Z
        elif Y == Z and Y >= X:
            A = X
            B = X
            C = Y
        else: # Z == X and Z >= Y
            A = Z
            B = Y
            C = Y
            
        print(f"{A} {B} {C}")