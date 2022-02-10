#include <iostream>
#include <random>

//0=front 1=back
int main() {
	std::random_device rnd{};
	int frontc = 0;
	int mixc = 0;
	int backc = 0;
	std::string error = "";
	for (int i = 0; i < 10; i++) {
		int coin = rnd() % 2;
		int coin1 = rnd() % 2;
		std::cout << coin << " "; //Debug
		std::cout << coin1 << "\n"; //Debug
		if (coin == 0 && coin1 == 0) {
			frontc++;
		}
		else if (coin == 0 && coin1 == 1) {
			mixc++;
		}
		else if (coin == 1 && coin1 == 0) {
			mixc++;
		}
		else if (coin == 1 && coin1 == 1) {
			backc++;
		}
		else {
			error = "Failed";
		}
	}

	//When Finish
	std::cout << "FrontSide: " << frontc << " "  << "BothSide: " << mixc << " " << "BackSide: " << backc++;
}
