#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int parents[100];

bool compare(vector<int> a, vector<int> b) { return a[2] < b[2]; }

int find_parent(int num){
    if (parents[num] != num)
        return parents[num] = find_parent(parents[num]);
    return num;
}

void union_node(int a, int b){
    a = find_parent(a);
    b = find_parent(b);

    if (a < b)
        parents[b] = a;
    else
        parents[a] = b;
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;

    for(int i=0; i<n; i++)
        parents[i] = i;

    sort(costs.begin(), costs.end(), compare);   

    for (int i=0; i<costs.size(); i++){
        if (find_parent(costs[i][0]) != find_parent(costs[i][1])){
            union_node(costs[i][0], costs[i][1]);
            answer+=costs[i][2];
        }
    }

    return answer;
}

int main(void){

    vector<vector<int>> v({
        {0,1,1},
        {0,2,2},
        {1,2,5},
        {1,3,1},
        {2,3,8}
    });

    cout<<solution(4, v)<<'\n';

    return 0;
}