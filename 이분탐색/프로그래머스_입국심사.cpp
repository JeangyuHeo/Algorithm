#include <bits/stdc++.h>

using namespace std;

long long solution(int n, vector<int> times) {
	long long answer = 0;
	long long min_time = 1;
	long long max_time = *max_element(times.begin(), times.end()) * (long long)n;

	while (min_time <= max_time) {
		long long cnt = 0;
		long long avg_time = (min_time + max_time) / 2;

		for (int i : times)
			cnt += avg_time / i;

		if (cnt >= n) {
			answer = avg_time;
			max_time = avg_time - 1;
		}
		else {
			min_time = avg_time + 1;
		}
	}

	return answer;
}

int main(void) {

	vector<int> v = { 7,10 };
	cout << solution(6, v) << '\n';

	return 0;
}