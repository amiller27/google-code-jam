/*
 * Aaron Miller
 * Google Code Jam 2015
 */
#include <iostream>
#include <sstream>
#include <stdio.h>

int main(int argc, char const *argv[])
{
	std::string endline;
	int N;
	std::cin >> N;
	getline(std::cin, endline);

	for (int testCase = 0; testCase < N; testCase++) {
		int sMax;
		std::cin >> sMax;

		int output = 0;
		int standing = 0;

		std::string line;
		getline(std::cin, line);
		for (int s = 0; s < sMax + 1; s++) {
			std::stringstream c(line.substr(s+1, 1));
			int nextS;
			c >> nextS;

			if (s > standing) {
				output += s - standing;
				standing = s;
			}
			standing += nextS;
		}

		printf("Case #%d: %d\n", testCase + 1, output);
	}
	return 0;
}
