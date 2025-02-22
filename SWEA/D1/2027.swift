// 주어진 텍스트를 그대로 출력하세요.


for i in 0..<5 {

    var a = Array(repeating: "+", count: 5)
    a[i] = "#"

    print(a.joined())
}