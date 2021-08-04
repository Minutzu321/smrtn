#include <iostream>

using namespace std;
// arm-linux-gnueabihf-g++ b.cpp -o program_test
int main(int argc, char** argv){
    if(argc==2){
        int a = atoi(argv[1]);
        switch(a){
            case 3:
                cout << "FUNCTIONEAZA";
                break;
            default:
                cout<<"EROARE. TREBUIE INTRODUS NUMARUL 1";
                break;
        }
    }else{
        cout<<"EROARE ARGUMENTE";
    }
    return 0;
}