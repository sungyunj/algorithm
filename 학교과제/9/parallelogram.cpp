#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

// 두 점 사이의 거리를 계산하는 함수
long long dist(int x1, int y1, int x2, int y2) {
    return (long long)(x2 - x1) * (x2 - x1) + (long long)(y2 - y1) * (y2 - y1);
}

// 네 점이 평행사변형을 이루는지 판단하는 함수
bool parallelogram(int ax, int ay, int bx, int by, int cx, int cy, int dx, int dy) {
    long long AB = dist(ax, ay, bx, by);
    long long BC = dist(bx, by, cx, cy);
    long long CD = dist(cx, cy, dx, dy);
    long long DA = dist(dx, dy, ax, ay);
    long long AC = dist(ax, ay, cx, cy);
    long long BD = dist(bx, by, dx, dy);

    // 평행사변형의 조건: 두 쌍의 대변이 각각 같거나, 대각선이 서로 같은 경우
    return (AB == CD && BC == DA) || (AC == BD);
}

int main() {
    ifstream inp("parallelogram.inp");
    ofstream out("parallelogram.out");

    int ax, ay, bx, by, cx, cy, dx, dy;

    while (inp >> ax >> ay >> bx >> by >> cx >> cy >> dx >> dy) {
        // 모든 좌표값이 0인 경우는 처리하지 않음
        if (ax == 0 && ay == 0 && bx == 0 && by == 0 && cx == 0 && cy == 0 && dx == 0 && dy == 0) {
            break;
        }

        if (parallelogram(ax, ay, bx, by, cx, cy, dx, dy)) {
            out << "1" << endl;
        } else {
            out << "0" << endl;
        }
    }

    inp.close();
    out.close();

    return 0;
}
