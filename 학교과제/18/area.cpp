#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

struct Circle {
    int x, y, r;
};

struct Point {
    double x, y;
};

bool pointsEqual(const Point& a, const Point& b) {
    const double DELTA_LIMIT = 1e-6;
    return fabs(a.x - b.x) < DELTA_LIMIT && fabs(a.y - b.y) < DELTA_LIMIT;
}

bool findIntersect(const Circle& c1, const Circle& c2, vector<Point>& points) {
    int diff_x = c2.x - c1.x;
    int diff_y = c2.y - c1.y;
    double dist = sqrt(diff_x * diff_x + diff_y * diff_y);

    if (dist > c1.r + c2.r || dist < abs(c1.r - c2.r) || dist == 0) return false;

    double a = (c1.r * c1.r - c2.r * c2.r + dist * dist) / (2 * dist);
    double h = sqrt(c1.r * c1.r - a * a);

    Point mid_point = {c1.x + diff_x * a / dist, c1.y + diff_y * a / dist};

    Point intersect1 = {mid_point.x + h * diff_y / dist, mid_point.y - h * diff_x / dist};
    Point intersect2 = {mid_point.x - h * diff_y / dist, mid_point.y + h * diff_x / dist};

    points.push_back(intersect1);
    if (!pointsEqual(intersect1, intersect2)) {
        points.push_back(intersect2);
    }
    return true;
}

double triangles(const Point& a, const Point& b, const Point& c) {
    return fabs(a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)) / 2.0;
}

bool circlePoints(const Point& p, const Circle& c) {
    return pow(p.x - c.x, 2) + pow(p.y - c.y, 2) <= pow(c.r, 2) + 1e-6;
}

int main() {
    ifstream inp("area.inp");
    ofstream out("area.out");
    int T;
    inp >> T;

    out << fixed << setprecision(2);
    while (T--) {
        Circle c1, c2, c3;
        inp >> c1.x >> c1.y >> c1.r;
        inp >> c2.x >> c2.y >> c2.r;
        inp >> c3.x >> c3.y >> c3.r;

        vector<Point> points;
        vector<Point> intersection;

        if (findIntersect(c1, c2, intersection) && findIntersect(c2, c3, intersection) && findIntersect(c3, c1, intersection)) {

            // Filtering points inside all circles
            vector<Point> insidePoints;
            for (size_t i = 0; i < intersection.size(); ++i) {
                const Point& p = intersection[i];
                if (circlePoints(p, c1) && circlePoints(p, c2) && circlePoints(p, c3)) {
                    insidePoints.push_back(p);
                }
            }

            // Assuming the validPoints can form a triangle
            if (insidePoints.size() >= 3) {
                double area = triangles(insidePoints[0], insidePoints[1], insidePoints[2]);
                out << area << endl;
            } else {
                out << "0.00" << endl;
            }
        } else {
            out << "0.00" << endl;
        }
    }

    inp.close();
    out.close();
    return 0;
}
