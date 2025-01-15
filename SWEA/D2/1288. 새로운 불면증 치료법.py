# 호석이는 불면증에 걸렸다. 그래서 잠이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다.
# 호석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다.

# 즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.
# 이렇게 숫자를 세던 호석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다.
# 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?

# 예를 들어 N = 1295이라고 하자.
# 첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.
# 두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.

# 현재까지 본 숫자는 0, 1, 2, 5, 9이다.
# 세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
# 네 번째로 4N = 5180번 양을 센다. 현재 본 숫자는 0, 1, 5, 8이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
# 다섯 번째로 5N = 6475번 양을 센다. 현재 본 숫자는 4, 5, 6, 7이다.

# 현재까지 본 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9이다.
# 5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 호석이는 양 세기를 멈춘다.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.

# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
# ( 호석이는 xN번 양을 세고 있다. )


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    seen_digits = set()  # 0에서 9까지 본 숫자를 저장할 집합
    k = 0  # 몇 번째 양을 셌는지 기록
    
    while len(seen_digits) < 10:  # 모든 숫자를 다 볼 때까지

        k += 1
        current_number = N * k  # 현재 k번째 양의 번호
        seen_digits.update(str(current_number))  # 숫자를 문자열로 변환해 자릿수를 추가

    
    print(f'#{test_case} {current_number}')