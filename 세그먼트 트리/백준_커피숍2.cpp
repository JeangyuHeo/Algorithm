#include <bits/stdc++.h>

using namespace std;

int n, q;
vector<long long> v;
long long tree[400001];

long long init(int start, int end, int node){
    if (start == end){
        return tree[node] = v[start];
    }

    int mid = (start + end) / 2;

    return tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1);
}

long long sum(int start, int end, int left, int right, int node){
    if (end < left || right < start) return 0;
    if (left <= start && right >= end) return tree[node];

    int mid = (start + end) / 2;

    return sum(start, mid, left, right, node * 2) + sum(mid + 1, end, left, right, node * 2 + 1);
}

void update(int start, int end, int node, int idx, long long diff){
    if (idx < start || idx > end)
        return;
    tree[node] += diff;

    if (start == end)
        return;

    int mid = (start + end) / 2;

    update(start, mid, node * 2, idx, diff);
    update(mid + 1, end, node * 2 + 1, idx, diff);
}

int main(){
    
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    cin >> n >> q;

    for (int i=0; i<n; i++){
        long long num;
        cin >> num;
        v.push_back(num);
    }
    
    init(0, n-1, 1);

    for (int i=0; i<q; i++){
        int x, y;
        long long a, b;
        cin >> x >> y >> a >> b;

        if (x <= y)
            cout << sum(0, n-1, x-1, y-1, 1) << '\n';
        else
            cout << sum(0, n-1, y-1, x-1, 1) << '\n';

        update(0, n-1, 1, a - 1, b - v[a-1]);

        v[a-1] = b;
    }

    return 0;
}