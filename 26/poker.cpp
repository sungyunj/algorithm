#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

const vector<string> results = {"Top", "One Pair", "Two Pair", "Triple", "Straight", "Flush", "Full House", "Four Card", "Straight Flush"};

int cardValue(char c) {
    if (c >= '2' && c <= '9') return c - '0';
    if (c == 'T') return 10;
    if (c == 'J') return 11;
    if (c == 'Q') return 12;
    if (c == 'K') return 13;
    if (c == 'A' || c == '1') return 14;  // 14 for A, handle 1 separately
    return -1;
}

vector<int> getCardValues(vector<string>& choice) {
    vector<int> values;
    for (auto& card : choice) {
        values.push_back(cardValue(card[1]));
    }
    sort(values.begin(), values.end());
    return values;
}

bool isFlush(vector<string>& choice) {
    char suit = choice[0][0];
    for (auto& card : choice) {
        if (card[0] != suit) return false;
    }
    return true;
}

bool isStraight(vector<int>& values) {
    for (int i = 0; i < 4; ++i) {
        if (values[i] + 1 != values[i + 1]) return false;
    }
    return true;
}

bool isStraight(vector<string>& choice) {
    vector<int> values = getCardValues(choice);
    if (isStraight(values)) return true;

    if (values[4] == 14) { // Check for A, 2, 3, 4, 5 straight
        values[4] = 1;
        sort(values.begin(), values.end());
        if (isStraight(values)) return true;
    }

    // Check for T, J, Q, K, 1 (treated as A) straight
    vector<int> Asame1Straight = {10, 11, 12, 13, 1};
    if (values == Asame1Straight) return true;

    return false;
}

int getChoicerank(vector<string>& choice) {
    vector<int> ranks = getCardValues(choice);
    map<int, int> rankCount;
    for (auto& rank : ranks) {
        rankCount[rank]++;
    }

    bool flush = isFlush(choice);
    bool straight = isStraight(choice);

    if (flush && straight) return 8; // Straight Flush

    int maxCount = 0, pairs = 0, triples = 0;

    for (auto& pair : rankCount) {
        if (pair.second == 4) return 7; // Four Card
        if (pair.second == 3) triples++;
        if (pair.second == 2) pairs++;
        maxCount = max(maxCount, pair.second);
    }

    if (triples && pairs) return 6; // Full House
    if (flush) return 5; // Flush
    if (straight) return 4; // Straight
    if (triples) return 3; // Triple
    if (pairs == 2) return 2; // Two Pair
    if (pairs == 1) return 1; // One Pair

    return 0; // Top
}

int main() {
    ifstream inp("poker.inp");
    ofstream out("poker.out");

    int T;
    inp >> T;

    while (T--) {
        vector<string> cards(7);
        for (int i = 0; i < 7; ++i) {
            inp >> cards[i];
        }

        int cardBest = 0;
        for (int i = 0; i < 7; ++i) {
            for (int j = i + 1; j < 7; ++j) {
                vector<string> choice;
                for (int k = 0; k < 7; ++k) {
                    if (k != i && k != j) {
                        choice.push_back(cards[k]);
                    }
                }
                cardBest = max(cardBest, getChoicerank(choice));
            }
        }

        out << results[cardBest] << endl;
    }

    inp.close();
    out.close();
    return 0;
}
