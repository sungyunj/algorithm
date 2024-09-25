#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

long long squareDistance(int x1, int y1, int x2, int y2) {
    return (long long)(x2 - x1) * (x2 - x1) + (long long)(y2 - y1) * (y2 - y1);
}

int main() {
    ifstream fin("triangle.inp");
    ofstream fout("triangle.out");

    int T;
    fin >> T;

    while (T--) {
        int x1, y1, x2, y2, x3, y3;
        fin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

        // Calculate the squared lengths of each side
        long long a2 = squareDistance(x2, y2, x3, y3); // BC^2
        long long b2 = squareDistance(x1, y1, x3, y3); // AC^2
        long long c2 = squareDistance(x1, y1, x2, y2); // AB^2

        // Check the type of triangle using the properties of its angles
        if (a2 == b2 + c2 || b2 == a2 + c2 || c2 == a2 + b2) {
            fout << 1 << endl; // Right angle triangle
        } else if (a2 > b2 + c2 || b2 > a2 + c2 || c2 > a2 + b2) {
            fout << 2 << endl; // Obtuse triangle
        } else {
            fout << 0 << endl; // Acute triangle
        }
    }

    fin.close();
    fout.close();
    return 0;
}
