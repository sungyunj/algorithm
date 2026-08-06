# 자연수로 구성된 두 집합 A와 B가 주어진다. 
# 두 집합 사이의 관계를 아래 네 개 중 하나로 구분하는 프로그램을 작성하라.

#     -  ‘=’: 두 집합 A와 B가 서로 같다.
#     -  ‘<’: A와 B는 서로 다르고, A가 B의 부분집합이다.
#     -  ‘>’: A와 B는 서로 다르고, B가 A의 부분집합이다.
#     -  ‘?’: 위의 세 분류에 모두 해당하지 않는다.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 각 테스트 케이스는 세 개의 줄로 이루어진다.
# 이 중 첫 번째 줄에는 집합 A의 크기와 집합 B의 크기가 공백 하나를 사이로 두고 주어진다.
# 두 번째 줄에는 집합 A의 원소들이 공백 하나씩을 사이로 두고 주어진다.
# 세 번째 줄에는 집합 B의 원소들이 공백 하나씩을 사이로 두고 주어진다.
# 집합의 크기는 집합의 원소의 개수를 의미하며, 1 이상 50 이하이다.
# 집합의 원소는 모두 1 이상 100 이하의 자연수이며, 한 집합 내에서 모든 원소는 서로 다르다.


# [출력]

# 각 테스트 케이스마다, 집합 A와 B 사이의 관계를 나타내는 문자를, 한 줄에 하나씩 출력한다.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/24420/1_sample_input.txt", "r")

T = int(input())

for _ in range(T):
    na, nb = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    if A == B:
        print("=")
    elif A < B:   # A가 B의 진부분집합
        print("<")
    elif A > B:   # B가 A의 진부분집합
        print(">")
    else:
        print("?")