#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

map<string, char> mapInit() {
    map<string, char> m;
    m["000000"] = 'A';
    m["001111"] = 'B';
    m["010011"] = 'C';
    m["011100"] = 'D';
    m["100110"] = 'E';
    m["101001"] = 'F';
    m["110101"] = 'G';
    m["111010"] = 'H';
    return m;
}

map<string, char> codeMap = mapInit();

int hamming(const string& s1, const string& s2) {
    int distance = 0;
    for (int i = 0; i < 6; i++) {
        if (s1[i] != s2[i]) {
            distance++;
        }
    }
    return distance;
}

string decodeM(const string& message) {
    string result = "";
    for (int i = 0; i < message.length(); i += 6) {
        string binary = message.substr(i, 6);
        char decode = 'X';
        for (map<string, char>::const_iterator it = codeMap.begin(); it != codeMap.end(); ++it) {
            int dist = hamming(binary, it->first);
            if (dist == 0 || dist == 1) {
                decode = it->second;
                break;
            }
        }
        result += decode;
    }
    return result;
}

int main() {
    ifstream inp("mail.inp");
    ofstream out("mail.out");

    int T;
    inp >> T;
    while (T--) {
        int n;
        string message;
        inp >> n >> message;
        string decode = decodeM(message);
        out << decode << endl;
    }
    inp.close();
    out.close();
    return 0;
}
