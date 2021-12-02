#include<iostream>
#include<vector>
#include<fstream>

int main(){

    int sum = 0;
    int x;
    std::vector<int> vec;
    std::ifstream inFile;

    inFile.open("in.txt");
    
    if (!inFile){
        std::cout << "Unable to open file";
        exit(1);
    }

    while (inFile >> x){
        vec.push_back(x);
    }
    
    unsigned int count = 0;
    
    for (unsigned int i = 0; i < vec.size() - 1; ++i){
        count += vec[i] < vec[i+1];
    }
    
    std::cout << "Task 1: " << count << std::endl;
    unsigned int count2 = 0;
    int x1,x2;
    for(unsigned int j = 0; j < vec.size() -3; ++j){
        x1 = vec[j] + vec[j+1] + vec[j+2];
        x2 = vec[j+1] + vec[j+2] + vec[j+3];
        count2 += x1 < x2;
    }
    std::cout << "Task 2: " << count2 << std::endl;
   
    inFile.close();
    return 0;
}
