# B개의 검은 공, W개의 흰 공, B개의 검은 상자, W개의 흰 상자가 있다.
# 당신은 모든 공을 상자에 담아서, 모든 상자가 정확히 한 개의 공을 담고 있도록 하고자 한다.

# 모든 공을 상자에 넣으면, 아래와 같이 각 상자마다 점수를 계산한다.
# 검은 상자에 검은 공이 들어 있으면 X점, 흰 상자에 흰 공이 들어 있으면 Y점, 검은 상자에 흰 공이 들어 있거나 흰 상자에 검은 공이 들어 있으면 Z점이다.

# 당신은 모든 상자의 점수의 합이 최대화되도록 공을 넣고자 한다. 이 때 얻을 수 있는 최대 점수를 구하는 프로그램을 작성하라.

 
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어진다.
# 각 줄에는 다섯 개의 정수 B, W, X, Y, Z (1 ≤ B, W ≤ 100, -1000 ≤ X, Y, Z ≤ 1000)가 공백 하나씩을 사이로 두고 주어진다.

 
# [출력]

# 각 테스트 케이스마다, 가능한 최대 점수 합을 출력한다.



import sys

sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/24396/1_sample_input.txt","r")

T = int(input())

for _ in range(T):
    B, W, X, Y, Z = map(int, input().split())

    # 가능한 최소한의 같은 색 배치
    if B >= W:
        ans = (B - W) * X + 2 * W * Z
    else:
        ans = (W - B) * Y + 2 * B * Z

    # 검은-검은 + 흰-흰 한 쌍을 추가했을 때의 이득
    gain = X + Y - 2 * Z

    if gain > 0:
        ans += min(B, W) * gain

    print(ans)