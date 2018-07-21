#include<iostream> 
#include<string> 

using namespace std; 

string quard(string::iterator& it) { 

  char head = *it; 
  ++it; 
  if (head == 'b' || head == 'w') 
	return string(1, head); 

  string LU = quard(it); 
  string RU = quard(it); 
  string LD = quard(it); 
  string RD = quard(it);
  return string("x")+LD+RD+LU+RU; }

int main() { 
  int num; 
  string str; 
  cin >> num; 
  while (num--) {
	cin >> str; string::iterator iter = str.begin(); 
	cout << quard(iter) << endl; 
  } 
}

