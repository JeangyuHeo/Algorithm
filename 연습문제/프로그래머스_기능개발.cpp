#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	int idx = 0;

	while (idx < progresses.size()) {
		int cnt = 0;
		
		for (int i = 0; i < progresses.size(); i++)
			progresses[i] += speeds[i];

		while (progresses[idx] >= 100 && idx < progresses.size()) {
			idx++;
			cnt++;
		}

		if (cnt != 0)
			answer.push_back(cnt);
		
	}

	return answer;
}

int main(void) {
	vector<int> progresses = { 93, 30, 55 };
	// {95, 90, 99, 99, 80, 99}
	vector<int> speeds = { 1, 30, 5 };
	// {1, 1, 1, 1, 1, 1}

	solution(progresses, speeds);

	
	return 0;
}