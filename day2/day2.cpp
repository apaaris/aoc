#include<iostream>
#include<vector>
#include<fstream>
#include<string.h>

int main(){

    int sum = 0;
    int x;
    //std::vector<string> vec(1000);
    std::ifstream inFile;

    inFile.open("in.txt");
    
    if (!inFile){
        std::cout << "Unable to open file";
        exit(1);
    }

    std::string order;
    unsigned int value;
    unsigned int hor = 0, pos = 0;

    while (inFile >> order >> value){
        if(order == "forward"){
            hor += value;
        }
        if(order == "down"){
            pos += value;
        }
        if(order == "up"){
            pos -= value;
        }
    } 
  // 
    std::cout <<"Task1: " << hor * pos << std::endl; 




  //  
    inFile.close();
    return 0;
}
