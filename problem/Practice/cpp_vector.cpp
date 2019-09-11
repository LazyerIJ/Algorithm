#include <iostream>
#include <vector>

using namespace std;

int main(){

    vector<int> v;
    v.reserve(8);
    cout<<"[*]vector.reserve(8)"<<endl;
    cout<<"[*]vector.push_back"<<endl;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);
    v.push_back(50);

    for (vector<int>::size_type i=0; i<v.size(); ++i)
        cout << v[i] << " ";

    cout<<endl;
    cout<<"size : "<<v.size()<<endl;
    cout<<"capacity : "<<v.capacity()<<endl;
    cout<<"max_size : "<<v.max_size()<<endl;

    cout<<endl<<"[*]resize(10)"<<endl;
    v.resize(10);
    for(vector<int>::size_type i=0; i<v.size(); ++i)
        cout<<v[i]<<" ";
    cout<<endl;


    cout<<endl<<"[*]resize(10)"<<endl;
    v.resize(3);
    for(vector<int>::size_type i=0; i<v.size(); ++i)
        cout<<v[i]<<" ";

    cout<<endl;
    cout<<"size : "<<v.size()<<endl;
    cout<<"capacity : "<<v.capacity()<<endl;
    cout<<"max_size : "<<v.max_size()<<endl;
    
    cout<<endl<<"[*]v.front()"<<endl;
    v.front()=1000;
    for(vector<int>::size_type i=0; i<v.size(); ++i)
        cout<<v[i]<<" ";
    cout<<endl; 

    cout<<endl<<"[*]v.pop_back()"<<endl;
    v.pop_back();
    for(vector<int>::size_type i=0; i<v.size(); ++i)
        cout<<v[i]<<" ";
    cout<<endl;

    cout<<endl;
    cout<<"[*]v.clear()"<<endl;
    v.clear();
    if(v.empty())
        cout<<"[*]vector is empty!!"<<endl;


    return 0;
}
