# 당신의 친구는 두 정수 A,B 를 마음 속으로 생각한 후, A+B 와 A-B 의 값을 불러주었다.
# 친구가 마음속으로 생각한 두 정수 A,B는 무엇일까?


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다. 
#     -  첫 번째 줄에 두 정수 X,Y 가 주어진다. (-100 ≤ X,Y ≤ 100).
#     -  A + B = X, A - B = Y 이다. 항상 답이 되는 정수 A,B 가 존재함이 보장된다.
 

# [출력]
# 각 테스트 케이스 마다 한 줄씩, 문제의 정답을 출력하라.

# import sys
# sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/26792/1_sample_input.txt","r")

TC = int(input())

for i in range(1, TC + 1):
    X, Y = map(int, input().split())

    A = (X + Y) // 2
    B = (X - Y) // 2

    print(f"{A} {B}")