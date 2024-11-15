#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

struct Point {
    long long x, y;
    
    bool operator <(const Point& p) const {
        return x < p.x || (x == p.x && y < p.y);
    }
};

long long cross(const Point& O, const Point& A, const Point& B) {
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

vector<Point> convexHull(vector<Point> P) {
    int n = P.size(), k = 0;
    if (n <= 3) return P;
    vector<Point> H(2*n);

    sort(P.begin(), P.end());

    for (int i = 0; i < n; ++i) {
        while (k >= 2 && cross(H[k-2], H[k-1], P[i]) <= 0) k--;
        H[k++] = P[i];
    }

    for (int i = n-1, t = k+1; i > 0; --i) {
        while (k >= t && cross(H[k-2], H[k-1], P[i-1]) <= 0) k--;
        H[k++] = P[i-1];
    }

    H.resize(k-1);
    return H;
}

int main() {
    ifstream inputFile("hull.inp");
    ofstream outputFile("hull.out");

    int n;
    inputFile >> n;

    vector<Point> points(n);
    for (int i = 0; i < n; ++i) {
        inputFile >> points[i].x >> points[i].y;
    }

    vector<Point> result = convexHull(points);
    outputFile << result.size() << '\n';
    for (size_t i = 0; i < result.size(); ++i) {
        outputFile << result[i].x << ' ' << result[i].y << '\n';
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
