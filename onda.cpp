#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <cmath>

using namespace std;

const float pi=3.141519265359;
const float c=0.5;
const float dt=0.01;
const float dx=0.01;
const float v=dx/dt;
const float T=6;
const float L=1;
const int Nt=T/dt + 1;
const int Nx=L/dx + 1;

void solucion(void);

int main(){
    solucion();
    return 0;
}

void solucion(void){
    float Y[Nx][Nt]={0};
    for(int i=1; i<Nx-1; i++){
            Y[i][0]=sin(i*pi/(Nx-1));
    }
    for(int i=1; i<Nx-1; i++){
            Y[i][1]=Y[i][0] + (c*c*0.5/(v*v))*(Y[i+1][0] + Y[i-1][0] - 2*Y[i][0]);
    }
    for(int j=1; j<Nt-1; j++){
        for(int i=1; i<Nx-1; i++){
            Y[i][j+1]=2*Y[i][j] - Y[i][j-1] + (c*c/(v*v))*(Y[i+1][j] + Y[i-1][j] - 2*Y[i][j]);
        }
    }
    ofstream outfile;
    outfile.open("datos.txt");
    for(int j=0; j<Nt;j++){
        for(int i=0;i<Nx;i++){
                outfile<<Y[i][j]<<endl;
        }
    }
    outfile.close();
    

}