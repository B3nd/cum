#include <iostream>


int fib(int number){
	int answer;
	if(number <= 2){
		answer =  1;
	} else{
		answer = fib(number - 1) + fib(number - 2);
	}

	return answer;
}

int main(){
	using namespace std;

	int num;

	cin >> num;

	cout << '\n';

	for (int i = 1; i <= num; i++){
		cout <<  i << ") " << fib(i) << '\n';
	}

}
