#include <bits/stdc++.h>

using namespace std;

int answer = 0;

void dfs(vector<int>& numbers, int target, int idx, int sum) {

	if (idx == numbers.size()) {
		if(sum == target)
			answer++;
		return;
	}

	dfs(numbers, target, idx + 1, sum + numbers[idx]);
	dfs(numbers, target, idx + 1, sum - numbers[idx]);
}

int solution(vector<int> numbers, int target) {
	dfs(numbers, target, 0, 0);

    return answer;
}

int main(void) {
	vector<int> v = { 1,1,1,1,1 };

	cout << solution(v, 3) << '\n';

	return 0;
}