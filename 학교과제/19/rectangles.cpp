#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>  // Include for multimap

using namespace std;

struct Event {
    int x, y1, y2, type;
    Event(int _x, int _y1, int _y2, int _type) : x(_x), y1(_y1), y2(_y2), type(_type) {}
};

// Comparator for sorting events
bool eventComparator(const Event& a, const Event& b) {
    if (a.x != b.x) return a.x < b.x;
    return a.type > b.type;
}

int main() {
    ifstream infile("rectangles.inp");
    ofstream outfile("rectangles.out");

    int n;
    infile >> n;
    vector<Event> events;

    for (int i = 0; i < n; ++i) {
        int x1, y1, x2, y2;
        infile >> x1 >> y1 >> x2 >> y2;
        events.push_back(Event(x1, y1, y2, 1));  // Start of rectangle
        events.push_back(Event(x2, y1, y2, -1)); // End of rectangle
    }

    // Sort events by x coordinate, then by type (end before start if same x)
    sort(events.begin(), events.end(), eventComparator);

    int current_x = 0, area = 0;
    multimap<int, pair<int, int> > activeIntervals;  // to store active y-intervals

    for (size_t i = 0; i < events.size(); ++i) {
        Event& e = events[i];
        if (i > 0) {
            int dx = e.x - current_x;
            if (!activeIntervals.empty() && dx > 0) {
                // Calculate the covered y-length in active intervals
                int total_y = 0;
                int last_y = -10001;  // outside possible range
                int current_cover_start = -10001, current_cover_end = -10001;

                for (multimap<int, pair<int, int> >::iterator it = activeIntervals.begin(); it != activeIntervals.end(); ++it) {
                    if (it->second.first > current_cover_end) {
                        if (current_cover_end != -10001) {
                            total_y += current_cover_end - current_cover_start;
                        }
                        current_cover_start = it->second.first;
                        current_cover_end = it->second.second;
                    } else if (it->second.second > current_cover_end) {
                        current_cover_end = it->second.second;
                    }
                }
                total_y += current_cover_end - current_cover_start;  // Add the last segment
                area += total_y * dx;
            }
        }
        current_x = e.x;

        if (e.type == 1) { // Starting a rectangle
            activeIntervals.insert(make_pair(e.y1, make_pair(e.y1, e.y2)));
        } else { // Ending a rectangle
            for (multimap<int, pair<int, int> >::iterator it = activeIntervals.begin(); it != activeIntervals.end(); ++it) {
                if (it->second.first == e.y1 && it->second.second == e.y2) {
                    activeIntervals.erase(it);
                    break;
                }
            }
        }
    }

    outfile << area << endl;
    infile.close();
    outfile.close();
    return 0;
}
