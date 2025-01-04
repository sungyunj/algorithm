// 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.


// [제약 사항]
// 월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.
// 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
// 두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.


// [입력]
// 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
// 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
// 첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.


// [출력]
// 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


import Foundation

let monthDays: [Int: Int] = [
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
]

if let T = Int(readLine()!) {
    for testCase in 1...T {
        
        let arr = readLine()!.split(separator: " ").compactMap { Int($0) }
        let startMonth = arr[0], startDay = arr[1], endMonth = arr[2], endDay = arr[3]
        
        var ans = 0

        if startMonth == endMonth {
            // 같은 달인 경우
            ans = endDay - startDay + 1
        } else {
            // 시작 월 남은 일수 추가
            ans += (monthDays[startMonth] ?? 0) - startDay + 1
            
            // 시작 월, 종료 월 사이 모든 월 일수 더함
            for month in (startMonth + 1)..<endMonth {
                ans += monthDays[month] ?? 0
            }

            // 종료 월 일수 추가
            ans += endDay
        }

        print("#\(testCase) \(ans)")
    }
}
