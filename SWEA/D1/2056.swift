// 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.


//     [그림1]    22220228  - >  2222/02/28  


// 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
// [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
// 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

// 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
// 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.


//     [표1]
//             1월  1 일 ~ 31 일   2월  1일 ~ 28 일

//             3월  1 일 ~ 31 일   4월  1일 ~ 30 일

//             5월  1 일 ~ 31 일   6월  1일 ~ 30 일

//             7월  1 일 ~ 31 일   8월  1일 ~ 31 일

//             9월  1 일 ~ 30 일   10월  1일 ~ 31 일   

//             11월  1 일 ~ 30 일   12월  1일 ~ 31 일

// ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


// [입력]
// 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
// 다음 줄부터 각 테스트 케이스가 주어진다.


// [출력]
// 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

// (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


import Foundation

let maxDays: [Int: Int] = [
    1: 31, 2: 28, 3: 31,
    4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30,
    10: 31, 11: 30, 12: 31
]

if let T = Int(readLine()!) {

    for t in 1...T {

        if let date = readLine(), date.count == 8, let month = Int(date[4..<6]), let day = Int(date[6..<8]) {

            let year = date.prefix(4)
            
            if let maxDay = maxDays[month], (1...maxDay).contains(day) {
                print("#\(t) \(year)/\(date[4..<6])/\(date[6..<8])")
            } 
            else {
                print("#\(t) -1")
            }
        }
    }
}


extension String {

    subscript(range: Range<Int>) -> String {
        
        let start = index(startIndex, offsetBy: range.lowerBound)
        let end = index(startIndex, offsetBy: range.upperBound)
        return String(self[start..<end])
    }
}