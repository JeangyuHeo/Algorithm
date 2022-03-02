#include <bits/stdc++.h>

using namespace std;

long long solution(int n) {
	long long d[60001];

	d[1] = 1;
	d[2] = 2;

	for (int i = 3; i <= n; i++)
		d[i] = (d[i - 1] + d[i - 2]) % 1000000007;
	
	return d[n];
}
int main(void) {

	cout << solution(4) << '\n';

	return 0;
 }