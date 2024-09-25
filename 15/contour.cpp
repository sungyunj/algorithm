#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
#define endl '\n'
#define ll long long
using namespace std;

ifstream fin;
ofstream fout;

struct node {
    int x, h, type;
    // node(int x, int h, int type) : x(x), h(h), type(type) {}
    bool operator<(const node& other) const { 
        if (x != other.x) return x < other.x;
        return type > other.type;  
    }
};

void solved(){
    vector<node> nodes;
    map<int, ll> areas; 
    vector<ll> areaValues;
    int l, h, r;
    int testCase = 1;
    while (fin >> l >> h >> r) {
        areaValues.clear();
        if (l == 0 && h == 0 && r == 0) {
            if (nodes.empty()) continue;
            map<int, int> activates;
            sort(nodes.begin(), nodes.end());

            int maxH = 0;
            ll prevX = nodes.front().x;
            
            for (const auto& node : nodes) {
                ll curX = node.x;
                if (curX != prevX) {
                    if (maxH > 0) areas[maxH] += curX - prevX;
                    else if(!areas.empty()){
                        ll area_sum = 0;
                        for (auto& area : areas) {
                            area_sum += area.first * area.second;
                        }
                        areas.clear();
                        areaValues.push_back(area_sum);
                    }
                    prevX = curX;
                }
                if (node.type == 1) activates[node.h]++;
                else if (--activates[node.h] == 0) activates.erase(node.h);

                if (!activates.empty()) maxH = activates.rbegin()->first;
                else  maxH = 0;
            }
            if (!areas.empty()) {
                ll area_sum = 0;
                for (auto& area : areas) {
                    area_sum += area.first * area.second;
                }
                areas.clear();
                areaValues.push_back(area_sum);
            }
            fout << "Test Case #" << testCase << " : ";
            for(auto& area : areaValues){
                fout << area << " ";
            }
            fout << endl;
            testCase++;
            nodes.clear();
            continue;
        }
        node tmp; tmp.x = l; tmp.h = h; tmp.type = 1;
        node tmp2; tmp2.x = r; tmp2.h = h; tmp2.type = -1;
        nodes.emplace_back(tmp);
        nodes.emplace_back(tmp2);
    }
}

int main() {
    fin.open("contour.inp");
    fout.open("contour.out");

    solved();
    
    fout.close();
    fin.close();
}
