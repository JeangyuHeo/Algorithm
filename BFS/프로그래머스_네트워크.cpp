#include <bits/stdc++.h>

using namespace std;

int visited[200];

void bfs(vector<vector<int>> computers, int n, int cur) {

	queue<int> q;

	for (int i = 0; i < n; i++) {
		if (computers[cur][i] && cur != i) {
			q.push(i);
			visited[i] = 1;
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int i = 0; i < n; i++) {
			if (computers[now][i] && !visited[i] && now != i) {
				q.push(i);
				visited[i] = 1;
			}
		}
	}
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;

	for (int i = 0; i < n; i++) {
		if (!visited[i]) {
			bfs(computers, n, i);
			answer++;
		}
	}

	return answer;
}

int main(void) {
	vector<vector<int>> v1 = {
		{1,1,0},
		{1,1,0},
		{0,0,1}
	};

	vector<vector<int>> v2 = {
		{1,1,0},
		{1,1,1},
		{0,1,1}
	};

	cout << solution(3, v2) << '\n';

	return 0;
}