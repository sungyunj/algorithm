#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <cmath>

using namespace std;

map<string, string> childParent; // 자식-부모 매핑을 위한 map

// 선조-후손 관계의 차수를 계산하는 유틸리티 함수
int findDegree(const string& start, const string& end) {
    int degree = 0;  // 차수를 저장할 변수
    string current = start;
    // 현재 위치가 목표(end)가 아니고, 현재 위치에 부모 정보가 있다면 계속 진행
    while (current != end && childParent.count(current) > 0) {
        current = childParent[current]; // 부모로 이동
        degree++;  // 차수 증가
        if (current == end) {
            return degree; // 목표에 도달했다면 차수 반환
        }
    }
    return -1; // 관계가 존재하지 않으면 -1 반환
}

// 최소 공통 조상 찾기
string findSA(string p, string q) {
    map<string, int> ancestor; // 조상을 저장할 map
    // p의 조상을 추적하면서 map에 저장
    while (p != "" && childParent.count(p)) {
        ancestor[p] = 1;
        p = childParent[p];
    }
    ancestor[p] = 1; // 루트 조상도 포함

    // q의 조상을 추적하면서 p의 조상 map에 이미 있는 조상이 나오면 반환
    while (q != "" && childParent.count(q)) {
        if (ancestor.count(q) > 0) {
            return q; // 공통 조상 발견
        }
        q = childParent[q];
    }
    if (ancestor.count(q)) {
        return q; // q가 루트 조상일 경우
    }
    return ""; // 공통 조상이 없는 경우
}

// 두 사람 사이의 관계를 찾는 함수
string findRelation(const string& p, const string& q) {
    if (p == q) {
        return "self"; // 자기 자신인 경우
    }

    int degreePQ = findDegree(p, q);
    if (degreePQ > 0) {
        if (degreePQ == 1) {
            return "child";
        } else if (degreePQ == 2) {
            return "grand child";
        } else {
            string relation = "great ";
            for (int i = 3; i < degreePQ; ++i) {
                relation += "great ";
            }
            relation += "grand child";
            return relation;
        }
    }

    int degreeQP = findDegree(q, p);
    if (degreeQP > 0) {
        if (degreeQP == 1) {
            return "parent";
        } else if (degreeQP == 2) {
            return "grand parent";
        } else {
            string relation = "great ";
            for (int i = 3; i < degreeQP; ++i) {
                relation += "great ";
            }
            relation += "grand parent";
            return relation;
        }
    }

    // 형제 관계 확인 (쉬운 경우의 사촌)
    if (childParent[p] == childParent[q]) {
        return "sibling";
    }

    // 사촌 관계 확인
    string sameAncestor = findSA(p, q);
    if (sameAncestor != "") {
        int m = findDegree(p, sameAncestor);
        int n = findDegree(q, sameAncestor);
        if (m > 0 && n > 0) {
            int k = min(m, n) - 1;  // k-th 사촌
            int j = abs(m - n);     // j번 제거
            if (j == 0) {
                return to_string(k) + " cousin";
            } else {
                return to_string(k) + " cousin removed " + to_string(j);
            }
        }
    }

    return "no relation"; // 관계 없음
}

int main() {
    ifstream inp("tree.inp");
    ofstream out("tree.out");

    string child, parent;
    // 파일에서 자식-부모 쌍 읽기
    while (inp >> child >> parent) {
        if (child == "no.child") break; // 'no.child'를 만나면 입력 종료
        childParent[child] = parent; // 매핑 정보 저장
    }

    string name1, name2;
    // 관계를 확인할 이름 쌍 읽기
    while (inp >> name1 >> name2) {
        string relation = findRelation(name1, name2); // 관계 찾기
        out << relation << endl; // 결과 출력
    }

    inp.close();
    out.close();
    return 0;
}
