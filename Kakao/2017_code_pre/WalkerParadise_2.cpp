//https://programmers.co.kr/learn/courses/30/lessons/1832
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int MOD = 20170805;
int solution(int m, int n, vector<vector<int>> city_map) {
    if ((n|m)==1) return 0;

    int routes[m][n][2];
    fill_n(&routes[0][0][0], m*n*2, 0);

    routes[0][0][0] = 1; // x
    routes[0][0][1] = 1; // y
    for (int x=0;x<m;x++) {
        for (int y=0;y<n;y++) {
            if ((x|y)==0) continue;
            int* route = &routes[x][y][0];
            int map = city_map[x][y];
            if (map == 0) {
                int cnt = 0;
                if (x > 0) cnt = routes[x-1][y][0];
                if (y > 0) cnt += routes[x][y-1][1];
                route[0] = route[1] = cnt%MOD;
            } else if (map == 1) {
                route[0] = route[1] = 0;
            } else if (map == 2) {
                if (x > 0) route[0] = routes[x-1][y][0];
                if (y > 0) route[1] = routes[x][y-1][1];
            }
        }
    }
    return routes[m-1][n-1][0];
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
