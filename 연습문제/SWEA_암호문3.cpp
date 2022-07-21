#include<iostream>
#include<list>

using namespace std;
int N, target, c_num;
char c_type;
list<int> encryptedList;
auto iter = encryptedList.begin();

int main(int argc, char** argv)
{
	for(int test_case = 1; test_case <= 10; ++test_case)
	{
        encryptedList.clear();
        iter = encryptedList.begin();
        
        scanf("%d",&N);
        
        for (int i=0; i<N; i++){
			scanf("%d", &target);
            encryptedList.push_back(target);
        }
        
        scanf("%d", &c_num);

        for(int i=0; i<c_num; i++){
            scanf(" %c", &c_type);

            int x,y,s;
            if (c_type == 'I'){
                iter = encryptedList.begin();
                list<int> temp;
                
                scanf("%d %d", &x, &y);
                for (int j=0; j<x; j++) iter++;
                for (int j=0; j<y; j++){
                    scanf("%d", &s);
                    temp.push_back(s);
                }
                encryptedList.splice(iter, temp);
            }
            else if (c_type == 'D'){
                iter = encryptedList.begin();
                scanf("%d %d", &x, &y);
                
                for(int j=0; j<x; j++) iter++;
                for(int j=0; j<y; j++) iter = encryptedList.erase(iter);
            }
            else if (c_type=='A'){
                scanf("%d", &y);
                for (int j=0; j<y; j++){
                    scanf("%d", &s);
                    encryptedList.push_back(s);
                }
            }
        }
        iter = encryptedList.begin();
        printf("#%d ", test_case);
        for (int i=0; i<10; i++)
            printf("%d ", *(iter++));
        printf("\n");
        
	}
	return 0;
}