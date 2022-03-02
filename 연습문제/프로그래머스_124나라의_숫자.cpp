#include <bits/stdc++.h>

using namespace std;

string solution(int n) {

	string answer = "";

	while (n != 0) {
		answer = "412"[n % 3] + answer;
		n = n / 3 - (n % 3 == 0);
	}

	return answer;
}

int main(void) {

	vector<int> ques = { 1, 2, 3, 4};
	
	for (int q : ques)
		cout<<solution(q)<<'\n';

	return 0;
}