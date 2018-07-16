//단체사진찍기
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
 
using namespace std;

int solution(int n, vector<string> data)
{
    string str = "ACFJMNRT";
    int permutation[] = {0,1,2,3,4,5,6,7};
    int answer = 0;
    do
    {
        bool flag = true;
        for (string& condition : data)
        {
            int num = condition[4]-'0';
            char op = condition[3];

            int dist = permutation[str.find(condition[0])] - permutation[str.find(condition[2])];
            dist = dist<0 ? -dist -1 : dist-1;
 
            if (op == '>' && !(dist > num)) flag = false;
            if (op == '=' && !(dist == num)) flag = false;
            if (op == '<' && !(dist < num)) flag = false;
 
            if (flag == false)
            {
                break;
            }
        }
        if (flag)
        {
            answer++;
        }
      
    } while (next_permutation(permutation, permutation + 8));
    return answer;
}
int main(){

    int answer = 0;
    vector<string> ques;
    ques.push_back("N~F=0");
    ques.push_back("R~T>2");

    answer = solution(2, ques);
    
    cout << answer;
    return 0;
}
