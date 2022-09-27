#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int solution(int n, vector<vector<int>> edge) {
	vector<vector<int>> map(n + 1, vector<int>(n + 1, 0));
	vector<int> dist(n + 1, INF);
	queue<int> q;
	int answer = 0;

	for (auto v : edge) {
		map[v[0]][v[1]] = 1;
		map[v[1]][v[0]] = 1;
	}

	q.push(1);
	dist[1] = 0;

	while (!q.empty()) {

		int val = q.front();
		int tmp_dist = dist[val] + 1;
		
		q.pop();

		for (int i = 1; i < n + 1; i++) {
			if (map[i][val]) {
				if (dist[i] > tmp_dist) {
					dist[i] = tmp_dist;
					q.push(i);
				}
			}
		}
	}

	sort(dist.begin(), dist.end());
	int max_val = *max_element(dist.begin(), dist.end()-1);

	for (int i = 1; i < n + 1; i++)
		if (max_val == dist[i])
			answer++;
	
	return answer;
}

int main(void) {

	vector<vector<int> > v = {
		{3,6},
		{4,3},
		{3,2},
		{1,3},
		{1,2},
		{2,4},
		{5,2}
	};

	cout << '\n' << solution(6, v) << '\n';

	return 0;
}