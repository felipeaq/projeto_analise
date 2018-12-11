#include <iostream>
#include "tabuleiro.hpp"
#include <cmath>
#include <vector>
using namespace std;


Tabuleiro::Tabuleiro(uint N){
  tam=1<<N;
  this->tabuleiro=vector<vector<char> >(tam,vector<char>(tam,(char)this->vazio));
}
void Tabuleiro::print_tabuleiro(){
  for (auto it = this->tabuleiro.begin();it!=this->tabuleiro.end();it++){
    for (auto jt = it->begin();jt!=it->end();jt++){
      cout<<*jt<<" ";
    }
    cout<<endl;
  }

  cout<<endl<<endl;


}


void Tabuleiro::print_tabuleiro(uint bi, uint ei,uint bj, uint ej){

  cout<<"bi="<<bi<<",   ei="<<ei<<"   ,bj="<<bj<<"   ,ej"<<ej<<endl;

    for (uint i=bi;i<ei;i++){
      for (uint j=bj;j<ej;j++){
        cout<<this->tabuleiro[i][j]<<" ";
      }
      cout<<endl;
    }



  cout<<endl<<endl;


}

void Tabuleiro::set_debug_mode(){
  uint count =60;
  for (uint i=0;i<tabuleiro.size();i++)
    for (uint j=0;j<tabuleiro[0].size();j++){

      tabuleiro[i][j]=count++;
    }
}

void Tabuleiro::set_val(uint i, uint j, char valor){
  this->tabuleiro[i][j]=valor;
}

void Tabuleiro::preencher(){
  this->dividir(0,this->tam,0,this->tam,this->tam);
}

void Tabuleiro::dividir(uint bi, uint ei,uint bj, uint ej,uint tam){

  print_tabuleiro(bi,ei,bj,ej);

  if (tam>2){
    uint metade =tam>>1;
    dividir(bi,  ei-metade, bj,  ej-metade, metade);
    dividir(bi+metade,  ei, bj,  ej-metade, metade);
    dividir(bi+metade,  ei, bj+metade,  ej, metade);
    dividir(bi,  ei-metade, bj+metade,  ej, metade);

  }else{

  }

}




int main(){
  uint N;
  cin>>N;
  Tabuleiro t=Tabuleiro(N);

  uint i,j;

  while(cin>>i>>j){


    t.set_val(i,j,t.buraco);
  }

  t.set_debug_mode();


  t.print_tabuleiro();
  t.preencher();
  //t.print_tabuleiro(t.tabuleiro.begin(),t.tabuleiro.end(),t.tabuleiro.begin()->begin(),(t.tabuleiro.end()-1)->end());


  return 0;
}
