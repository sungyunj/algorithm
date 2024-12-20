// N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
// 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

// [제약 사항]
// 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
// 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


// [입력]
// 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
// 다음 줄부터 각 테스트 케이스가 주어진다.
// 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
// 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
// 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


// [출력]
// 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
// (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import Foundation

if let T = Int(readLine()!) {
    
    for testCase in 1...T {
        // N과 K 입력
        let firstLine = readLine()!.split(separator: " ").compactMap { Int($0) }
        let N = firstLine[0]
        let K = firstLine[1]
        
        // 퍼즐 보드 입력
        var board: [[String]] = []
        for _ in 0..<N {
            let row = readLine()!.split(separator: " ").map { String($0) }
            board.append(row)
        }
        
        let matchString = String(repeating: "1", count: K)

        var rowCount = 0
        for row in board {
            let strRow = row.joined().components(separatedBy: "0")
            rowCount += strRow.filter { $0 == matchString }.count
        }
        
        // 열 순회
        var colCount = 0
        for col in 0..<N {
            let column = (0..<N).map { board[$0][col] }
            let strCol = column.joined().components(separatedBy: "0")
            colCount += strCol.filter { $0 == matchString }.count
        }

        print("#\(testCase) \(rowCount + colCount)")
    }
}
