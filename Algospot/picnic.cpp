/*
https://algospot.com/judge/problem/read/PICNIC
*/
#include <iostream>
#include <cstring>

using namespace std;

bool pairs[10][10];
int num_friends;
int num_pairs;

int countPairs(bool taken[10]){
    int firstpoint = -1;
    for(int i=0; i<num_friends; i++){
        if(!taken[i]){
            firstpoint=i;
            break;
        }
    }

    if(firstpoint==-1)
        return 1;

    int result=0;

    for(int i=firstpoint+1;i<num_friends;i++){
        if(!taken[i] && pairs[firstpoint][i]){
            taken[i] = taken[firstpoint] = true;
            result += countPairs(taken);
            taken[i] = taken[firstpoint] = false;
        }
    }

    return result;
}

int main(){

    int test_case;
    int num_case;

    cin >> test_case;

    for(int step=0; step<test_case; step++){
        cin >> num_friends >> num_pairs;

        for(int pair=0; pair<num_pairs; pair++){
            int n,m;
            cin >> n >> m;
            pairs[n][m] = pairs[m][n] = true;
        }

        bool taken[10];
        memset(taken,0,sizeof(taken));
        num_case = countPairs(taken);
        cout << num_case;
    }

    return 0;
}
