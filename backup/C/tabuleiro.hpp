#include <vector>




class Tabuleiro{


  public:

    void preencher ();
    void set_val(uint i, uint j,char valor);
    Tabuleiro(uint N);
    void print_tabuleiro();

    const char buraco='@';
    const char vazio ='*';
    const char preenchido='#';

    void set_debug_mode();
    void print_tabuleiro(uint bi, uint ei,uint bj, uint ej);
    std::vector<std::vector<char> > tabuleiro;


  private:
    void dividir(uint bi, uint ei,uint bj, uint ej,uint tam);

    uint tam;
};
