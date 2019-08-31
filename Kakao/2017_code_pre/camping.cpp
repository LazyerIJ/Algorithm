#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int solution(int n, vector<vector<int>> data) {
    int answer = 0;

    sort(data.begin(), data.end());
   
    for(int i=0; i<n; i++){
        for(int j=i; j<n; j++){
            if(data[i][0] != data[j][0] && data[i][1] != data[j][1]){
                answer++;
                for(int k=i; k<=j; k++){
                    bool dist_x1 = data[k][0] < max(data[i][0],data[j][0]);
                    bool dist_x2 = data[k][0] > min(data[i][0],data[j][0]);
                    bool dist_y1 = data[k][1] < max(data[i][1],data[j][1]);
                    bool dist_y2 = data[k][1] > min(data[i][1],data[j][1]);
                    if(dist_x1 && dist_x2 && dist_y1 && dist_y2){
                        answer--;
                        break;
                    }

                }
            }
        }
    }
    return answer;
}
