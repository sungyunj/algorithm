// 크기가 N인 파스칼의 삼각형을 만들어야 한다.

// 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

// 1. 첫 번째 줄은 항상 숫자 1이다.
// 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

// N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


// [제약 사항]

// 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


// [입력]

// 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
// 각 테스트 케이스에는 N이 주어진다.


// [출력]

// 각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
// 삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
// (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import Foundation

func pascal(_ n: Int) -> [[Int]] {
    var triangle: [[Int]] = []
    
    for i in 0..<n {
        var row = Array(repeating: 1, count: i + 1) // 각 줄은 1로 시작하고 끝남
        
        for j in 1..<i {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j] // 왼쪽 위와 오른쪽 위 숫자의 합 계산
        }
        triangle.append(row)
    }
    
    return triangle
}

if let T = Int(readLine()!) {
    for t in 1...T {
        if let input = readLine(), let N = Int(input), (1...10).contains(N) {
            // 파스칼의 삼각형 생성
            let pascalsTriangle = pascal(N)
            
            print("#\(t)")
            for row in pascalsTriangle {
                print(row.map { String($0) }.joined(separator: " "))
            }
        } else {
            print("N 값은 1 이상 10 이하의 정수")
        }
    }
}
