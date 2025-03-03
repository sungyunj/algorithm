# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.


T = int(input())
result = 1

if T < 30:
    for i in range(1, T+1):

        print(result, end = ' ')
        result *= 2