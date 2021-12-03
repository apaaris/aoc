#include<iostream>
#include<vector>
#include<fstream>
#include<string.h>
#include<cmath>

int main(){

    std::string x;
    std::vector<std::string> vec(1000);
    std::ifstream inFile;
    inFile.open("in.txt");
    
    if (!inFile){
        std::cout << "Unable to open file";
        exit(1);
    }
	unsigned int it = 0;
    
	while (inFile >> x){
	   vec.at(it) = x;
	   ++it; 
    }
   // vec is back in town
	std::vector<unsigned int> gm, ep;
   unsigned int gamma,epsilon;
   unsigned int sm = 0;
   for(unsigned int j = 0; j < vec.at(0).size(); ++j){
   sm = 0;
   for(unsigned int i = 0; i < vec.size(); ++i){
   sm += (vec.at(i).at(j) - 48) == 1;
   
   if (sm >= 500){
   gamma = 1;
   epsilon = 0;
   }
   else {
   gamma = 0;
   epsilon = 1;
   }
   }
   gm.push_back(gamma);
   ep.push_back(epsilon);
   }

   unsigned int x1 = 0;
   unsigned int x2 = 0;
    

	//Get significant bit
	//Sum 
	//Keep only the important ones
	//multiply
	//
	// Inefficient nested loops go brr
	//
	//
    unsigned int matching,max,idx;
    for(unsigned int i = 0; i < vec.size(); ++i){
    matching = 0;
    for(unsigned int j = 0; j < vec.at(0).size(); ++j){
    if(vec.at(i).at(j) - 48 == gm.at(j)){
    ++matching;
    }
    else{
    break;
    }
    }
    if(matching > max){
    matching = max;
    idx = i;}
    }
    unsigned int matching2,max2,idx2;
    for(unsigned int i = 0; i < vec.size(); ++i){
    matching2 = 0;
    for(unsigned int j = 0; j < vec.at(0).size(); ++j){
    if(vec.at(i).at(j) - 48 == ep.at(j)){
    ++matching2;
    }
    else{
    break;
    }
    }
    if(matching2 > max2){
    matching2 = max2;
    idx2 = i;}
    }
    std::vector<int> res2; 
    std::vector<int> res; 
   for(unsigned int k = 0; k < gm.size(); ++k){
   res.push_back(vec.at(idx).at(k) - 48);
   res2.push_back(vec.at(idx2).at(k) - 48);
   std::cout << vec.at(idx).at(k) - 48 << std::endl;
   } 
  unsigned int ox = 0; 
  unsigned int co = 0; 
   for(int i = gm.size()-1; i >= 0; --i){
    x1 +=  gm.at(i) * std::pow(2, gm.size() - 1 - i);
    x2 +=  ep.at(i) * std::pow(2, gm.size() - 1 - i);
    ox +=  res.at(i) * std::pow(2, gm.size() - 1 - i);
    co += res2.at(i) * std::pow(2, gm.size() -1 - i);
    }
    std::cout << "Task 1: " << x1 * x2 << std::endl;
    std::cout << "Task 2: " << ox*co << std::endl;

    inFile.close();
    return 0;
}
