/*
 * Aaron Miller
 * Google Code Jam 2015
 */
#include <algorithm>
#include <iostream>
#include <list>
#include <stdio.h>

int main(int argc, char const *argv[])
{
	std::string endline;
	int N;
	std::cin >> N;
	getline(std::cin, endline);

	for (int testCase = 0; testCase < N; testCase++) {
		int D;
		std::cin >> D;
		std::list<int> pancakes;
		for (int i = 0; i < D; i++) {
			int next;
			std::cin >> next;
			pancakes.push_back(next);
		}
		pancakes.sort();

		int output = 0;
		
		int c = 0;
		while (pancakes.size() > 0) {
			if (c++ == 100) break;
			int PMax = pancakes.back();
			int DMax = 0;
			int PNext = 0;
			for (std::list<int>::reverse_iterator rit = pancakes.rbegin(); rit != pancakes.rend(); rit++) {
				if (*rit >= PMax - 1 + (PMax%2)) {
					DMax++;
				} else {
					PNext = *rit;
					break;
				}
			}

			std::cerr << std::endl;
			for (std::list<int>::iterator it = pancakes.begin(); it != pancakes.end(); it++) {
				std::cerr << *it << std::endl;
			}
			if (PMax >= PNext + DMax && DMax <= PMax/2) {
				int DNextIfOdd = 0;
				for (int i = 0; i < DMax; i++) {
					if (pancakes.back() != PMax) {
						DNextIfOdd++;
					}
					pancakes.pop_back();
				}
				if (PNext <= (PMax+1)/2) {
					// split in half
					std::list<int>::const_iterator it = pancakes.cend();
					while (true) {
						if (*it <= (PMax-1)/2) {
							it++;
							break;
						} else {
							if (it == pancakes.begin()) {
								break;
							}
							it--;
						}
					}
					for (int i = 0; i < DNextIfOdd; i++) {
						pancakes.insert(it, (PMax-1)/2);
					}
					for (int i = 0; i < DMax - DNextIfOdd; i++) {
						pancakes.insert(it, PMax/2);
					}
					for (int i = 0; i < DMax; i++) {
						pancakes.insert(it, (PMax+1)/2);
					}
				} else {
					// split, but not in half
					std::list<int>::const_iterator it = pancakes.cbegin();
					while (it != pancakes.cend() && *it < PMax - PNext) {
						it++;
					}
					for (int i = 0; i < DNextIfOdd; i++) {
						pancakes.insert(it, PMax - PNext - 1);
					}
					for (int i = 0; i < DMax - DNextIfOdd; i++) {
						pancakes.insert(it, PMax - PNext);
					}

					while (it != pancakes.cend() && *it < PMax) {
						it++;
					}
					for (int i = 0; i < DMax; i++) {
						pancakes.insert(it, PNext);
					}
				}
				output += DMax;
			} else {
				// don't split
				for (std::list<int>::iterator it = pancakes.begin(); it != pancakes.end(); it++) {
					(*it)--;
				}
				while (!pancakes.empty() && pancakes.front() == 0) {
					pancakes.pop_front();
				}
				output++;
			}
			std::cerr << PMax << " " << PNext << " " << DMax << " " << output << std::endl;
		}

		printf("Case #%d: %d\n", testCase + 1, output);
	}
	return 0;
}
