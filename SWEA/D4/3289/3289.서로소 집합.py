# 초기에 {1}, {2}, ... {n} 이 각각 n개의 집합을 이루고 있다.
# 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
# 연산을 수행하는 프로그램을 작성하시오.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에 n(1≤n≤1,000,000), m(1≤m≤100,000)이 주어진다.
# m은 입력으로 주어지는 연산의 개수이다.
# 다음 m개의 줄에는 각각의 연산이 주어진다.
# 합집합은 0 a b의 형태로 입력이 주어진다.
# 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.
# 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.
# 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
# a와 b는 n 이하의 자연수이며 같을 수도 있다.


# [출력]
# 각 테스트 케이스마다 1로 시작하는 입력에 대해서 같은 집합에 속해있다면 1을, 아니면 0을 순서대로 한줄에 연속하여 출력한다.



# Find 연산: 루트 노드를 찾고 경로를 압축함
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # 한 줄로 경로 압축!
    return parent[x]

# Union 연산: 두 집합을 합침
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

# 메인 로직
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)] # 자기 자신으로 초기화
    
    ans = []
    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                ans.append('1')
            else:
                ans.append('0')
    
    print(f"#{tc} {''.join(ans)}")