#include <iostream>

using namespace std;
int binarySearch(int data[], int start, int end, int key){
    int mid = (int)((start+end)/2);

    while(1){
        if (data[mid]<key){
            return binarySearch(data,mid+1, end,key);
        }
        else if(data[mid]>key){
            return binarySearch(data,start,mid-1,key);
        }
        else if (data[mid]==key){
            return mid;
        }
        if (start>end)
            return -1;
    }
}

int main(){
    int data[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14};
    int n = sizeof(data) / sizeof(int);
    int key;

    cout<<"[+]Input Key: ";
    cin>>key;

    int start= 0;
    int end= n;

    int index=binarySearch(data,start,end,key);

    if(index==-1){
        cout <<"[*]can not find!!"<<endl;
    }
    else{
        cout<<"[*]Key   : " << key << endl;
        cout<<"[*]Index : " << index<<endl;
    }
    return 0;
}
