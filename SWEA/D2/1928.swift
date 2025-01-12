// 다음과 같이 Encoding 을 한다.

// 1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
// 2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.

// 입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.

// [제약사항]
// 문자열의 길이는 항상 4의 배수로 주어진다.
// 그리고 문자열의 길이는 100000을 넘지 않는다.

// [입력]
// 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
// 다음 줄부터 각 테스트 케이스가 주어진다.
// 테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.

// [출력]
// 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
// (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import Foundation

let base64Table = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

if let T = Int(readLine()!) {
    var results: [String] = []
    
    for t in 1...T {
        if let encodedString = readLine() {
            var temp = ""
            
            // Base64 문자 6비트 바이너리로 변환
            for char in encodedString {
                if let index = base64Table.firstIndex(of: char) {
                    temp += String(index, radix: 2).leftPadded(to: 6)
                }
            }
            
            // 디코딩된 원문
            var decodedString = ""
            var currentIndex = temp.startIndex
            
            while currentIndex < temp.endIndex {
                let nextIndex = temp.index(currentIndex, offsetBy: 8, limitedBy: temp.endIndex) ?? temp.endIndex
                let binaryString = String(temp[currentIndex..<nextIndex])
                if let asciiValue = Int(binaryString, radix: 2), let scalar = Unicode.Scalar(asciiValue) {
                    decodedString.append(Character(scalar))
                }
                currentIndex = nextIndex
            }
            
            results.append("#\(t) \(decodedString)")
        }
    }
    
    results.forEach { print($0) }
}

extension String {
    /// 문자열을 주어진 길이로 왼쪽에 0을 추가하여 패딩 처리
    func leftPadded(to length: Int) -> String {
        let paddingCount = max(0, length - self.count)
        return String(repeating: "0", count: paddingCount) + self
    }
}
