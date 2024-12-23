# C, C++, Python, Java 등의 언어에는 += 연산자가 있다. 
# 정수형 변수 x, y가 있을 때 “x += y”를 하면 x에 저장된 값이 (기존에 x에 저장되어 있던 값) + (기존에 y에 저장되어 있던 값)으로 바뀐다.


# 현재 x에 저장된 값은 A, y에 저장된 값은 B이다. 당신은 “x += y” 또는 “y += x” 연산을 원하는 순서대로 원하는 만큼 수행하여, x나 y 둘 중 하나 이상에 저장된 값이 N 초과가 되게 하려고 한다. 
# 연산을 합쳐서 최소 몇 번 수행해야 하는지 계산하는 프로그램을 작성하라.


# 입력

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어진다. 각 줄에는 세 개의 정수 A, B, N (1 <= A, B <= N <= 10^9)이 공백 하나씩을 사이로 두고 주어진다.
# 테스트 케이스의 개수는 600,000개 이상으로 상당히 많음에 유의하라.

 
# 출력

# 각 테스트 케이스마다, 한 줄에 하나씩 x나 y 둘 중 하나 이상에 저장된 값이 N 초과가 되게 하기 위해 “x += y”, “y += x” 연산을 최소 몇 번 수행해야 하는지 출력한다.


def min_operations(A, B, N):
    x, y = A, B
    count = 0
    while x <= N and y <= N:
        if x < y:
            x += y
        else:
            y += x
        count += 1
    return count


if __name__ == "__main__":
    T = int(input())
    results = []
    
    for _ in range(T):
        A, B, N = map(int, input().split())
        results.append(min_operations(A, B, N))
    
    print()
    for result in results:
        print(result)




# def min_operations(test_cases):
#     results = []
#     for A, B, N in test_cases:
#         x, y = A, B
#         count = 0
#         while x <= N and y <= N:
#             if x < y:
#                 x += y
#             else:
#                 y += x
#             count += 1
#         results.append(count)
#     return results


# import sys
# input = sys.stdin.read
# data = input().splitlines()

# T = int(data[0])
# test_cases = [tuple(map(int, line.split())) for line in data[1:]]

# results = min_operations(test_cases)
# sys.stdout.write('\n'.join(map(str, results)) + '\n')
