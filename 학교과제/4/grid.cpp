#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

using namespace std;

const long long MOD = 1000000007;
const int MAX_SIZE = 1001; // 격자의 최대 크기

int grid[MAX_SIZE][MAX_SIZE]; // 격자 상태를 저장
long long dp[MAX_SIZE][MAX_SIZE][11];

int main() {
    ifstream inputFile("grid.inp");
    ofstream outputFile("grid.out");

    int T; // 테스트 케이스의 수
    inputFile >> T;

    while (T--) {
        int x, y, a, b, k; // 격자의 크기, 장애물의 수, 이동 가능한 최대 횟수
        inputFile >> x >> y >> a >> b >> k;

        memset(grid, 0, sizeof(grid)); // 격자 초기화
        memset(dp, 0, sizeof(dp)); // 다이나믹 프로그래밍 배열 초기화

        // 장애물 위치 입력받아 표시
        for (int i = 0; i < a; ++i) {
            int posX, posY;
            inputFile >> posX >> posY;
            grid[posX][posY] = 1; // 장애물 표시
        }

        // 벽 위치 입력받아 표시
        for (int i = 0; i < b; ++i) {
            int posX, posY;
            inputFile >> posX >> posY;
            grid[posX][posY] = -1; // 벽 표시
        }

        dp[0][0][0] = 1; // 시작점의 값 설정

        for (int i = 0; i <= x; ++i) {
            for (int j = 0; j <= y; ++j) {
                for (int m = 0; m <= k; ++m) {
                    if (grid[i][j] == -1) continue; // 벽인 경우 스킵

                    int newM = min(m + grid[i][j], k); // 새로운 이동 가능한 최대 횟수 계산

                    // 이전 위치에서 현재 위치로 이동하는 경우의 수 계산
                    if (i > 0) dp[i][j][newM] = (dp[i][j][newM] + dp[i-1][j][m]) % MOD;
                    if (j > 0) dp[i][j][newM] = (dp[i][j][newM] + dp[i][j-1][m]) % MOD;
                }
            }
        }

        long long result = 0;
        for (int m = k; m <= k; ++m) {
            result = (result + dp[x][y][m]) % MOD;
        }

        outputFile << result << endl;
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
