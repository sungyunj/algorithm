# 1부터 N까지의 자연수 번호가 붙은 N명의 농구 선수가 있다.
# 두 농구팀 A팀과 B팀은, 각각 N명의 선수들에 순위를 매겨 놓았다.

# A팀은 선수들을 A_1, A_2, ···, A_N 순서대로 뽑고자 하고,
# B팀은 선수들을 B_1, B_2, ···, B_N 순서대로 뽑고자 한다.

# 즉, A_i 는 A팀이 i번째로 선호하는 선수의 번호이고, B_i 는 B팀이 i번째로 선호하는 선수의 번호이다.
# 두 팀은 A팀부터 시작하여 번갈아가면서 선수를 한 명씩 선발한다.
# 각 팀은 아직 선발되지 않은 선수 중 자기 팀에서 가장 지명 순위가 높은 선수를 선발할 예정이다.

# 두 팀의 선호 순서가 주어질 때, 모든 선발이 끝나고 각 선수가 어떤 팀에 속해 있는지를 구하는 프로그램을 작성하라.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 세 개의 줄로 이루어진다.
# 첫 번째 줄에는 선수의 수 N (1 ≤ N ≤ 50) 이 주어진다.
# 두 번째 줄에는 A_1, A_2, ···, A_N 이 공백 하나씩을 사이로 두고 주어진다.
# 세 번째 줄에는 B_1, B_2, ···, B_N 이 공백 하나씩을 사이로 두고 주어진다.

 
# [출력]
# 각 테스트 케이스마다, 길이 N의 문자열 S를 출력한다.
# S의 i번째 글자는, i번 선수가 A팀에 의해 선발되었으면 ‘A’,
# B팀에 의해 선발되었으면 ‘B’여야 한다.


# 입력 예제             출력 예제  
# 2                   AAB
# 3                   ABBABA
# 1 2 3
# 3 2 1
# 6
# 1 4 2 6 3 5
# 2 3 1 6 5 4



import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/23791/1_sample_input.txt","r")

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    used = [False] * (N + 1)
    answer = [''] * N

    a = 0
    b = 0

    for turn in range(N):
        if turn % 2 == 0:
            # A팀 차례
            while used[A[a]]:
                a += 1

            player = A[a]
            used[player] = True
            answer[player - 1] = 'A'
            a += 1

        else:
            # B팀 차례
            while used[B[b]]:
                b += 1

            player = B[b]
            used[player] = True
            answer[player - 1] = 'B'
            b += 1

    print(''.join(answer))