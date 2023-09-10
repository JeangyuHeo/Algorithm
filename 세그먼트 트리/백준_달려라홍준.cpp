#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> v;
int tree[4000001];

int init(int start, int end, int node){
    if (start == end) return tree[node] = v[start];

    int mid = (start + end) / 2;

    return tree[node] = max(init(start, mid, node *2), init(mid +1, end, node * 2 + 1));
}

int find_max(int start, int end, int node, int left, int right){
    if (left > end || right < start) return 0;

    if (left <= start && right >= end) return tree[node];

    int mid = (start + end) / 2;

    return max(find_max(start, mid, 2*node, left, right), find_max(mid+1, end, 2*node+1, left, right));
}

int main(){

    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    cin>>n>>m;

    for(int i=0; i<n; i++){
        int num;

        cin>>num;

        v.push_back(num);
    }

    init(0, n-1, 1);

    for (int i=m-1; i<=(n-m); i++){
        cout<<find_max(0, n-1, 1, i - (m-1), i + (m-1))<<' ';
    }
    cout<<'\n';

    return 0;
}