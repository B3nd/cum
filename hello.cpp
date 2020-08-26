#include <iostream>

int fib(int number){
	if(number == 1 || number == 2){
		return 1;
	}else {
		return fib(number - 1) + fib(number - 2);
	}
}

int main(){
	using namespace std;

	int number, answer;

	cin >> number;

	answer = fib(number);

	cout << answer << '\n';

	return 0;

}
