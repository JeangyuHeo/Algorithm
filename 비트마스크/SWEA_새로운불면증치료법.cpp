#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;

	cin>>T;
	
	for(test_case = 1; test_case <= T; ++test_case)
	{

        int n;
        cin>>n;
        int i=n, t=0;
        
        while (true) {
            int k = i;
            while(k){
                t |= (1 << (k % 10));
                k /= 10;
            }
            if ( t== 1023)
                break;
            i+= n;
        }
            
        cout<<"#"<<test_case<<" "<<i<<'\n';
	}
    
	return 0;
}