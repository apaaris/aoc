#include<iostream>
#include<vector>
#include<fstream>
#include<string.h>

int main(){

    std::ifstream inFile;

    inFile.open("in.txt");
    
    if (!inFile){
        std::cout << "Unable to open file";
        exit(1);
    }

    std::string order;
    unsigned int value;
    unsigned int hor = 0, pos = 0, aim = 0;

    while (inFile >> order >> value){
        if(order == "forward"){
            hor += value;
            pos += aim * value;
            
        }
        if(order == "down"){
            //pos += value;
            aim += value;
        }
        if(order == "up"){
            //pos -= value;
            aim -= value;
        }
    } 
    std::cout <<"Task2: " << hor * pos << std::endl; 


    inFile.close();
    return 0;
}
