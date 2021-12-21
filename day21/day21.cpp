#include<iostream>

int dieNext = 1;

int roll() {

    int val = dieNext;
    if (dieNext == 100){
	    dieNext = 1;
    }
    else ++dieNext;

    return val;
}

int roll3() {
    return roll() + roll() + roll();
}

void update(int pos) {
    pos += roll3();
    pos %= 10;
    if (pos == 0){
	    pos = 10;
    }
}


void part1(const unsigned int A, const unsigned int B){
	unsigned int posA = A;
	unsigned int posB = B;
	unsigned int scoreA = 0;
	unsigned int scoreB = 0;
	unsigned int times = 0;
	while(true){
		times += 3;
	update(posA);
	scoreA += posA;
	if(scoreA >= 1000){
	update(posB);
	std::cout << scoreB << std::endl;
	scoreB += posB;
	}
	if(scoreB >= 1000){
	break;
	}
	}
	std::cout << std::min(scoreA,scoreB)*(times+1) << std::endl;	
	return;
}

int main(){
const auto inA = 10;
const auto inB = 7;

part1(inA,inB);
	
return 0;
}


