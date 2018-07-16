#include <vector>
#include <iostream>

using namespace std;
bool isrange(int x,int y, int x_max, int y_max){

    if((x>=0&&x<x_max) &&(y>=0&&y<y_max))
        return true;
    return false;

}

int isSameArea(int cur_x, int cur_y,int m_x, int m_y, 
                    vector<vector<int>> flag, vector<vector<int>> picture,int cur_area){

    int dx[]={1,-1,0,0};
    int dy[]={0,0,1,-1};
    if (isrange(cur_x, cur_y,m_x,m_y)){
        if(picture[cur_x][cur_y]==0 && flag[cur_x][cur_y]==0){
            cur_area++; 
            for(int k=0; k<4; k++){
                isSameArea(cur_x+dx[k], cur_y+dy[k],m_x,m_y,flag,picture,cur_area);
            }
        }
    }
    return cur_area;

}

vector<int> solution(int m, int n, vector<vector<int>> picture) {

    int number_of_area = 0;
    int max_size_of_one_area = 0;



    //탐색 체크 벡터 
    vector<vector<int>> flag;

    for(int i=0; i<m; i++){
        cout<<"a";
        vector<int> flag_zero(n);
        flag.push_back(flag_zero);
        for(int j=0; j<n; j++){
            flag[i][j]=0;
        }
    }
        
    //전방향 순회
    for(int i=0;i <m; i++){
        for(int j=0; j<n; j++){
            cout<<"a";
            int area=0;
            area = isSameArea(i,j,m,n,flag,picture,area);
            if (area>0){
                number_of_area++;
                max_size_of_one_area = area ? area>max_size_of_one_area : max_size_of_one_area;    
            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;

}

int main(){

    int n=5;
    int m=5;
    vector<vector<int>> arr;
    vector<int> result;

    vector<int> element1 = {0,1,1,1,0};
    vector<int> element2 = {0,1,0,1,1};
    vector<int> element3 = {0,0,1,0,0};
    vector<int> element4 = {1,0,1,1,0};
    vector<int> element5 = {0,0,1,0,1};

    arr.push_back(element1);
    arr.push_back(element2);
    arr.push_back(element3);
    arr.push_back(element4);
    arr.push_back(element5);

    cout<<endl;

    result =solution(5, 5, arr);
    return 0;
}
