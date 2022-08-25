#include <bits/stdc++.h>

using namespace std;

int solution(string name) {
	int answer = 0, i = 0;
	string joy_name(name.length(), 'A');
	int length = name.length();

	while (true) {
		joy_name[i] = name[i];
		
		answer += min(name[i] - 'A', 'Z' - name[i] + 1);

		if (name == joy_name)
			break;

		for (int j = 1; j < length; j++) {
			if (name[(i + j) % length] != joy_name[(i + j) % length]) {
				i = (i + j) % length;
				answer += j;
				break;
			}
			if (name[(length + i - j) % length] != joy_name[(length + i - j) % length]) {
				i = (length + i - j) % length;
				answer += j;
				break;
			}
		}
	}


	return answer;
}

int main(void) {
	
	vector<string> v = { 
		"JEROEN",
		"JAN"
	};

	for (string s : v)
		cout << solution(s) << '\n';

	return 0;
}