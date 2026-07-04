# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.


import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/4834/sample_input.txt","r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cards = input()
    
    # 0부터 9까지 숫자의 개수를 저장 카운팅 배열 (크기 10)
    count = [0] * 10
    
    # 각 숫자의 등장 횟수 세기
    for card in cards:
        count[int(card)] += 1
        
    max_card = 0  # 가장 많은 카드의 숫자
    max_count = 0 # 가장 많은 카드의 장수
    
    # 0부터 9까지 확인하며 최댓값 갱신
    # 장수가 같을 때는 숫자가 큰 쪽을 선택해야 하므로, 
    # 부등호를 '>'가 아닌 '>='로 설정하여 같은 장수일 때 더 큰 숫자로 갱신되도록 함.
    for i in range(10):
        if count[i] >= max_count:
            max_count = count[i]
            max_card = i
            
    print(f"#{test_case} {max_card} {max_count}")