//https://programmers.co.kr/learn/courses/30/lessons/1831
#include <cmath>
#include <iostream>
#define getMaxStar(n) (int(log(n)/log(3)))

using namespace std;

int isPossibleTone(int leftlength, int tone, int flag){

    int result=0;  
    if(leftlength<0 || flag>0)
        return 0;
    if(tone==3 && flag==-2)
        return 1;
    if(tone%3==0)
        result += isPossibleTone(leftlength-1, tone/3, flag+2);
    result += isPossibleTone(leftlength-1, tone-1 ,flag-1);
    
    return result;
}

int solution(int n) {
    int answer = 0;
    int maxLength = getMaxStar(n)*3;
    answer= isPossibleTone(maxLength,n,0);
    return answer;
}

int main(){

    int hightone = 41;
    int result = solution(hightone);
    
    cout<<"[*]result : "<<result<<endl;
    return 0;
}
