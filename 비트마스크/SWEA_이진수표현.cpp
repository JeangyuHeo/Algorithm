#include<iostream>
#include<string>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;
	
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n,m, bit_num=0;
        string res="ON";
        
        cin>>n>>m;
        
        for (int i=n-1; i>=0; i--)
            if (!(m & (1 << i)))
                res = "OFF";
        
        cout<<"#"<<test_case<<" "<<res<<"\n";
	}
	return 0;
}