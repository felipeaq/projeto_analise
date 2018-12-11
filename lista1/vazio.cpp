#include <bits/stdc++.h>

using namespace std;


bool verifica_repetidos(vector<int> v){
  auto max=max_element(v.begin(),v.end());
  vector<bool> bin(*max,false);
  for (int i =0;i<v.size();i++){
    if (bin[v[i]])
      return false;
    bin[v[i]]=true;
  }
  return true;

}

int main(){

  vector<int> v = {2,4,5,5,3333,3};
  vector<int> v2 = {5,43,22,2,1};


  cout<<verifica_repetidos(v)<<" "<<verifica_repetidos(v2)<<endl;

  return 0;
}
