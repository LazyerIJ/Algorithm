#include <vector>
#include <iostream>
#include <cstring>

using namespace std;
vector<vector<int>> arr;

bool isrange(int x,int y, int x_max, int y_max){
    if(x<0 || x>=x_max || y<0 || y>=y_max)
        return false;
    return true;
}

int isSameArea(int x, int y, int m, int n, int color){

    if(!isrange(x,y,m,n) || color!=arr[x][y])
        return 0;

    int dx[]={1,-1,0,0};
    int dy[]={0,0,1,-1};
    int size=1;
    arr[x][y]=0;

    for(int i=0;i<4; i++){ 
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        size += isSameArea(new_x,new_y,m,n,color);
    }
    return size;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area=0;
    int max_size_of_one_area=0;
    arr = picture;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(arr[i][j]==0)
                continue;
            number_of_area++;
            int area=isSameArea(i,j,m,n,arr[i][j]);
            max_size_of_one_area = (area>max_size_of_one_area)?area:max_size_of_one_area;
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;

}

int main(){
    int m=6;
    int n=4;
    
    vector<vector<int>> arr;
    vector<int> result(2);

    vector<int> element1 = {1,1,1,0};
    vector<int> element2 = {1,2,2,0};
    vector<int> element3 = {1,0,0,1};
    vector<int> element4 = {0,0,0,1};
    vector<int> element5 = {0,0,0,3};
    vector<int> element6 = {0,0,0,3};
    
    arr.push_back(element1);
    arr.push_back(element2);
    arr.push_back(element3);
    arr.push_back(element4);
    arr.push_back(element5);
    arr.push_back(element6);

    result =solution(m,n, arr);

    cout<<result[0]<<endl;
    cout<<result[1]<<endl;

    

    return 0;
}
