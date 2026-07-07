# ‘A’, ‘T’, ‘C’, ‘G’ 로 이루어진 길이 N의 DNA 수열 S가 있다.

# 길이가 L인 두 DNA 수열 X, Y가 반전 관계 라는 것은,
# 모든 1 ≤ i ≤ L에 대해, X의 i번째 문자와 Y의 i번째 문자가 서로 반전 관계에 있음을 뜻한다.
# ‘A’는 ‘T’ 와 서로 반전 관계고, ‘C’ 는 ‘G’와 서로 반전 관계이다.

# 다음과 같은 조건을 만족하는 정수 쌍 1≤i≤j≤N 의 개수를 출력하라.
# -   S의 i번째 문자부터 j번째 문자까지를 순서대로 만든 문자열을 T라고 할 때,
#     T의 문자들을 섞어서 T와 반전 관계에 있는 문자열을 만들 수 있다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
# 각 테스트 케이스는 다음과 같이 구성되었다. 
# -  첫 번째 줄에 문자열의 길이 N과 길이 N의 문자열 S가 공백으로 구분되어 주어진다.
# -  S의 문자는 ‘A’, ‘T’, ‘C’, ‘G’ 중 하나이다. (1≤N≤5000)
 

# [출력]
# 각 테스트 케이스 마다 한 줄씩, 문제의 정답을 출력하라.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D3/26837/1_sample_input.txt","r")

def solve():
    tc = int(input())
    
    for _ in range(tc):
        # 각 테스트 케이스의 첫 줄에서 N과 문자열 S를 동시에 입력받습니다.
        # 예: "5 ATCGT" -> N = 5, S = "ATCGT"
        line = input().split()
        N = int(line[0])
        S = line[1]
        
        # (diff_at, diff_cg)의 빈도수를 저장할 딕셔너리
        count_map = {(0, 0): 1}
        diff_at = 0
        diff_cg = 0
        ans = 0
        
        for char in S:
            if char == 'A':
                diff_at += 1
            elif char == 'T':
                diff_at -= 1
            elif char == 'C':
                diff_cg += 1
            elif char == 'G':
                diff_cg -= 1
                
            current_state = (diff_at, diff_cg)
            
            if current_state in count_map:
                ans += count_map[current_state]
                count_map[current_state] += 1
            else:
                count_map[current_state] = 1
                
        print(ans)

if __name__ == '__main__':
    solve()