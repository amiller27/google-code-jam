/*
 * Aaron Miller
 * Google Code Jam 2015
 */
#include <iostream>
#include <stdio.h>

int main(int argc, char const *argv[])
{
	std::string endline;
	int N;
	std::cin >> N;
	getline(std::cin, endline);

	for (int i = 0; i < N; i++) {
		int OUTPUT = 5 * i;

		printf("Case #%d: %d\n", i + 1, OUTPUT);
	}
	return 0;
}
