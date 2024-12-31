// N x N 행렬이 주어질 때,
// 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


// [제약 사항]
// N은 3 이상 7 이하이다.

// [입력]
// 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
// 각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
// 다음 N 줄에는 N x N 행렬이 주어진다.

// [출력]
// 출력의 첫 줄은 '#t'로 시작하고,
// 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
// 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
// (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import Foundation

if let T = Int(readLine()!) {
    for test in 1...T {
        if let N = Int(readLine()!) {
            var field: [[Int]] = []

            // 입력 배열 생성
            for _ in 0..<N {
                let row = readLine()!.split(separator: " ").compactMap { Int($0) }
                field.append(row)
            }

            // 90도, 180도, 270도 회전 행렬 생성
            var rotated90: [[Int]] = Array(repeating: Array(repeating: 0, count: N), count: N)
            var rotated180: [[Int]] = Array(repeating: Array(repeating: 0, count: N), count: N)
            var rotated270: [[Int]] = Array(repeating: Array(repeating: 0, count: N), count: N)

            for i in 0..<N {
                for j in 0..<N {
                    rotated90[i][j] = field[N - 1 - j][i]
                    rotated180[i][j] = field[N - 1 - i][N - 1 - j]
                    rotated270[i][j] = field[j][N - 1 - i]
                }
            }

            // 결과 출력
            print("#\(test)")
            for i in 0..<N {
                let row90 = rotated90[i].map { String($0) }.joined()
                let row180 = rotated180[i].map { String($0) }.joined()
                let row270 = rotated270[i].map { String($0) }.joined()
                print("\(row90) \(row180) \(row270)")
            }
        }
    }
}
