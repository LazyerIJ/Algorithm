#include <iostream>
#include <algorithm>
#include <cstring>


using namespace std;

const int INF = 987654321;
int length;
int arr[100], partSum[100], partSquareSum[100];
int cache[100][10];

void preCalculate(void){

    /*정렬 및 순차합, 순차제곱 합 계산*/
    sort(arr,arr+length);
    partSum[0] = arr[0];
    partSquareSum[0] = arr[0] * arr[0];
    for(int i=0; i<length; i++){
        partSum[i] = partSum[i-1] + arr[i];
        partSquareSum[i] = partSquareSum[i-1] + arr[i]*arr[i];
    }
}

int minDifference(int low, int high){

    /*순차합, 순차제곱합을 이용한 MSE loss 계산*/
    int sum = partSum[high] - (low==0?0:partSum[low-1]);
    int squareSum = partSquareSum[high] - (low==0?0:partSquareSum[low-1]);
    int mean = (int)(0.5+(double)sum/(high-low+1));
    int result = squareSum + (high-low+1)*mean*mean - (2*mean*sum);

    return result;
}

int quantize(int from, int parts){

    /*기저사례*/
    if (from==length)
        return 0;
    if (parts==0)
        return INF;

    /*캐시확인*/
    int result = cache[from][parts];
    if (result!=0)
        return result;

    result = INF;
    for (int partSize=1; from+partSize<=length; partSize++){
        /*재귀호출*/
        result = min(result,minDifference(from,from+partSize-1)+quantize(from+partSize,parts-1));
        /*캐시저장*/
        cache[from][parts] = result;
    }

    return result;

}

int main(){

    int test_case;
    int parts;
    int result;

    cin >> test_case;

    for(int step=0; step<test_case; step++){
        cin >> length >> parts;
        for(int i=0; i<length; i++)
            cin >> arr[i];
        preCalculate();
        result = quantize(0,parts);
        /*캐시초기화*/
        memset(cache,-1, sizeof(cache));    
        cout<<result;
    }



    return 0;
}

    

