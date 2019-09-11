//https://programmers.co.kr/learn/courses/30/lessons/1832
#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

int MOD = 20170805;
int hori[501][501];
int verti[501][501];

int solution(int m, int n, vector<vector<int>> city_map) {
    memset(hori, 0, sizeof hori);
    memset(verti, 0, sizeof verti);
    hori[1][1] = 1;
    verti[1][1] = 1;

    for(int i=1; i<=m;i++){   
        for(int j=1;j<=n;j++){
            if(city_map[i-1][j-1]==0){

                hori[i][j] += (hori[i][j-1] + verti[i-1][j])%MOD;
                verti[i][j] += (hori[i][j-1] + verti[i-1][j])%MOD;


            }
            else if(city_map[i-1][j-1]==1){
                hori[i][j] = 0;
                verti[i][j] = 0; 
            }
            else{
                hori[i][j] = hori[i][j-1];
                verti[i][j] = verti[i-1][j];                                
            }
        }
    }

    return (hori[m][n-1]+verti[m-1][n])%MOD;
}

int main(){
    int m=3;
    int n=6;
    
    vector<vector<int>> arr;
    

    vector<int> element1 = {0,2,0,0,0,2};
    vector<int> element2 = {0,0,2,0,1,0};
    vector<int> element3 = {1,0,0,2,2,0};
    
    arr.push_back(element1);
    arr.push_back(element2);
    arr.push_back(element3);

    int result =solution(m,n, arr);

    cout<<result<<endl;

    return 0;
}
