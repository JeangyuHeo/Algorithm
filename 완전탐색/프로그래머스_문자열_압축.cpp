#include <bits/stdc++.h>
#define INF 1e9

using namespace std;

int solution(string s) {

	int answer = INF;
	int size = 0;

	while (size++ < s.length()) {
		int cnt = 0;

		string new_str;
		string tmp = s.substr(0, size);

		for (int i = 0; i < s.length(); i += size) {
			if (tmp == s.substr(i, size))
				cnt++;
			else {
				if (cnt != 1)
					new_str += to_string(cnt) + tmp;
				else
					new_str += tmp;
				tmp = s.substr(i, size);
				cnt = 1;
			}
		}
		if (cnt != 1)
			new_str += to_string(cnt) + tmp;
		else
			new_str += tmp;
		answer = min(answer, (int)new_str.length());
	}
	return answer;
}

int main(void) {
	vector<string> questions = {
		"aabbaccc",
		"ababcdcdababcdcd",
		"abcabcdede",
		"abcabcabcabcdededededede",
		"xababcdcdababcdcd"
	};

	for (string q : questions)
		cout << (solution(q)) << '\n';
	
	return 0;
}