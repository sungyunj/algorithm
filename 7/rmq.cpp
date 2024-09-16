#include <iostream>
#include <fstream>
#define endl '\n'
#define mod 100000
#define MAX 9000000000
using namespace std;

int tree[4000001]; // 세그먼트 트리 배열
long long v[1000001]; // 입력 배열
int n; // 입력 배열의 크기

// 세그먼트 트리 생성 함수
void segmentTree(int start, int end, int node);
// 쿼리 함수
int query(int start, int end, int l, int r, int node);
// 업데이트 함수
void update(int start, int end, int node, int idx);

int main(){
    ifstream inp;
    ofstream out;
    inp.open("rmq.inp"); // 입력 파일 열기
    out.open("rmq.out"); // 출력 파일 열기

    inp >> n; // 배열 크기 읽기
    v[n] = MAX; // 입력 배열의 마지막 값은 최대값으로 초기화
    for(int i = 0; i < n; i++) inp >> v[i]; // 입력 배열 읽기
    segmentTree(0, n, 1); // 세그먼트 트리 생성

    long long result = 0;

    // 쿼리 및 업데이트 처리
    while(1){
        char c; long long l, r;
        inp >> c; inp >> l >> r; // 쿼리 또는 업데이트 명령 읽기
        if( c == 'q' ) result += query(0, n, l, r, 1); // 쿼리 처리
        else if( c == 'c'){ // 업데이트 처리
            v[l] = r; // 해당 인덱스의 값을 업데이트
            update(0, n, 1, l); // 세그먼트 트리 업데이트
        }else{ // 종료 조건
            out << result % mod << endl; // 결과 출력
            break; // 반복 종료
        }
    }
    out.close(); // 출력 파일 닫기
    inp.close(); // 입력 파일 닫기
}

// 세그먼트 트리 생성 함수
void segmentTree(int start, int end, int node){
    if(start == end){ // 리프 노드인 경우
        tree[node] = start; // 현재 노드에 인덱스 할당
        return;
    }
    int mid = (start + end) / 2;

    segmentTree(start, mid, node*2); // 왼쪽 자식 노드 생성
    segmentTree(mid+1, end, node*2 +1); // 오른쪽 자식 노드 생성

    // 자식 노드 중에서 더 작은 값을 가진 노드를 현재 노드에 할당
    if(v[tree[node*2]] > v[tree[node*2+1]]) tree[node] = tree[node*2 + 1];
    else tree[node] = tree[node*2];
}

// 쿼리 함수
int query(int start, int end, int l, int r, int node){
    if(start > r || l > end) return n; // 범위가 겹치지 않는 경우

    if(start >= l && end <= r) return tree[node]; // 범위가 완전히 포함되는 경우

    int mid = (start+end) / 2;
    int l_child = query(start, mid, l, r, node*2); // 왼쪽 자식 노드 탐색
    int r_child = query(mid+1, end, l, r, node*2+1); // 오른쪽 자식 노드 탐색

    // 자식 노드 중에서 더 작은 값을 반환
    if(v[l_child] > v[r_child]) return r_child;
    else return l_child;
}

// 업데이트 함수
void update(int start, int end, int node, int idx){
    if(start == end){ // 리프 노드인 경우
        tree[node] = idx; // 현재 노드에 인덱스 할당
        return;
    }

    int mid = (start + end) / 2;  
    if(idx <= mid) update(start, mid, node*2, idx); // 왼쪽 자식 노드 업데이트
    else update(mid+1, end, node*2+1, idx); // 오른쪽 자식 노드 업데이트

    // 자식 노드 중에서 더 작은 값을 가진 노드를 현재 노드에 할당
    if(v[tree[node*2]] > v[tree[node*2+1]]) tree[node] = tree[node*2 +1];
    else tree[node] = tree[node*2];
}
