#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer(prices.size());
	stack<int> st;

	for (int i = 0; i < prices.size(); i++) {
		while (!st.empty() && prices[st.top()] > prices[i]) {
			answer[st.top()] = i - st.top();

			st.pop();
		}
		
		st.push(i);
	}

	while (!st.empty()) {
		answer[st.top()] = prices.size() - st.top() - 1;

		st.pop();
	}

	return answer;
}

int main(void) {

	vector<int> v = { 1,2,3,2,3 };

	vector<int> ans = solution(v);

	for (int i : ans)
		cout << i << ' ';
	cout << '\n';

	return 0;
}