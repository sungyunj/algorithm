// 주어진 숫자만큼 # 을 출력해보세요.

// 주어질 숫자는 100,000 이하다.

if let T = readLine(), let num = Int(T) {

    print(String(repeating: "#", count: num))
}
