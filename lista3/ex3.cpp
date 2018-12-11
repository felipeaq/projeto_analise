#include <iostream>
#include <vector>


using namespace std;
void printVec(std::vector<bool> v){
  for (unsigned int i=0;i<v.size();i++){
    cout<<v[i]<<", ";
  }

  cout<<endl;
}

int main(){
  int N=10;
  vector<bool> v(2*N,false);

  for (int i=0;i<N*2;i++){
    if (i%2==0){
      v[i]=true;
    }
  }

  printVec(v);

  for (unsigned int i=0;i<v.size();i++){
    for (unsigned j=i;j<v.size()-1-i;j++){
      swap(v[j],v[j+1]);
      printVec(v);
    }
  }


  return 0;
}
