# 준환이는 N개의 서로 다른 무게를 가진 무게 추와 양팔저울을 가지고 있다.
# 모든 무게 추를 양팔저울 위에 올리는 순서는 총 N!가지가 있고,
# 여기에 더해서 각 추를 양팔저울의 왼쪽에 올릴 것인지 오른쪽에 올릴 것인지를 정해야 해서 총 2^N * N!가지의 경우가 있다.
# 하지만 양팔 저울에 갑자기 문제가 생겨서 무게 추를 올릴 때 오른쪽 위에 올라가 있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 더 커져서는 안 된다.
# 예를 들어 무게추가 총 3개, 무게가 각각 1, 2, 4 라고 하면 아래 그림처럼 총 15가지 경우가 나올 수 있다.

# pic1 = '3234.png'

# 이런 방법으로 준환이가 양팔 저울에 모든 무게추를 올리는 방법은 총 몇 가지가 있을까?


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스마다 첫 번째 줄에 N(1 ≤ N ≤ 9)가 주어진다.
# 두 번째 줄에는 각 무게추의 무게를 의미하는 N개의 자연수가 공백으로 구분되어 주어진다. 무게는 1이상 999이하이다.


# [출력]
# 각 테스트 케이스마다 무게추를 올리는 과정에서 오른쪽 위에 올라가있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 커지지 않는 경우의 수를 출력한다.

 

# 1. 빈 리스트를 만들기
fac = [1] * 10
pow2 = [1] * 10
# 팩토리얼(!)과 2의 거듭제곱을 미리 계산
# N은 최대 9까지니까 10개씩 만들어두자.
for i in range(1,10):
    fac[i] = fac[i-1] * i
    pow2[i] = pow2[i-1] * 2

def scale(cnt, left, right, remain):
    global ans
    
    # [가지치기 추가] 
    # 남은 무게(remain)를 몽땅 오른쪽에 더해도 왼쪽(left)보다 작거나 같다?
    # 남은 추들을 나열하는 순서(fac)와 왼/오 선택(pow2)을 한 번에 계산해서 더함
    if left >= right + remain:
        ans += fac[N - cnt] * pow2[N - cnt]
        return

    # 모든 추를 다 올렸을 때 (규칙을 다 지켰다는 뜻)
    if cnt == N:
        ans += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            
            # 1. 왼쪽에 올리기 (남은 총 무게에서 지금 무게를 빼서 전달)
            scale(cnt + 1, left + weights[i], right, remain - weights[i])
            
            # 2. 오른쪽에 올리기 (조건 확인)
            if right + weights[i] <= left:
                scale(cnt + 1, left, right + weights[i], remain - weights[i])
            
            visited[i] = False

# 실행 부분
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    
    visited = [False] * N
    ans = 0
    # 전체 무게의 합을 미리 구해서 remain 인자로 넣어줘
    total_weight = sum(weights)
    
    scale(0, 0, 0, total_weight)
    print(f"#{t} {ans}")