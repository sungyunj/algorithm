# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.

# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 
# 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.

# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.


# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

import sys
sys.stdin = open("/Users/tjddbsj/Desktop/github/algorithm/algorithm/SWEA/D2/4866/sample_input.txt","r")

T = int(input())
for tc in range(1, T + 1):
    line = input()
    stack = []
    result = 1

    for char in line:
        # 1. 여는 괄호는 스택에 저장
        if char =='{' or char =='(':
            stack.append(char)
        # 2. 닫는 괄호들
        elif char == '}':
            if not stack or stack.pop() != '{':
                result = 0
                break
        
        elif char == ')':
            if not stack or stack.pop() != '(':
                result = 0
                break
# 3. 문자열을 다 돌았는데 스택에 여는 괄호가 남아있는 경우
    if stack:
        result = 0

    print(f"#{tc} {result}")