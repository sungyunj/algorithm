// 주어진 숫자부터 0까지 순서대로 찍어보세요

// 아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다.
// N N-1 N-2 ... 0



if let input = readLine(), let T = Int(input) {

    for i in stride(from: T, through: 0, by: -1) {
        print(i, terminator:" ")
    }
    print()
}

