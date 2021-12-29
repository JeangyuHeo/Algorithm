#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int brown, int yellow) {
	vector<int> answer;
	queue<int> q;
	int area = brown + yellow;

	q.push(3);

	while (true) {
		int height = q.front();
		
		q.pop();

		if (area % height == 0) {
			int width = area / height;
			if ((width - 2) * (height - 2) == yellow) {
				answer.push_back(width);
				answer.push_back(height);
				break;
			}
		}
		q.push(height + 1);
	}

	return answer;
}

int main(void) {

	vector<int> v1 = solution(10, 2);
	vector<int> v2 = solution(8, 1);
	vector<int> v3 = solution(24, 24);

	for (int i : v1)
		cout << i << ' ';
	cout << '\n';

	for (int i : v2)
		cout << i << ' ';
	cout << '\n';

	for (int i : v3)
		cout << i << ' ';
	cout << '\n';

	return 0;
}