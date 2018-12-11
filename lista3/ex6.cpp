#include <iostream>
#include <vector>


using namespace std;
int main(){
  string palavra;
  cin>>palavra;
  char a='A',b='B';
  int mult=0;
  int sum=0;
  for (auto it=palavra.begin();it!=palavra.end();it++){
    if (*it==a){
      mult++;
    }else if(*it==b){
      sum+=mult;
    }

  }
  cout<<sum<<endl;

  return 0;
}
