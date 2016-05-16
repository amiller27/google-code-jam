/*
 * Aaron Miller
 * Google Code Jam 2015
 */
#include <iostream>
#include <stdio.h>

int* A = new int[4] {1, 0, 0, 0};
int* I = new int[4] {0, 1, 0, 0};
int* J = new int[4] {0, 0, 1, 0};
int* K = new int[4] {0, 0, 0, 1};

int* mult(int* a, int* b)
{
	return new int[4] {
		a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3],
		a[0] * b[1] + a[1] * b[0] + a[2] * b[3] - a[3] * b[2],
		a[0] * b[2] + a[2] * b[0] + a[3] * b[1] - a[1] * b[3],
		a[0] * b[3] + a[3] * b[0] + a[1] * b[2] - a[2] * b[1]
	};
}

int* evaluate(std::string expr)
{
	int* result = A;
	for (int i = 0; i < expr.length(); i++) {
		if (expr[i] == 'i') {
			result = mult(result, I);
		} else if (expr[i] == 'j') {
			result = mult(result, J);
		} else if (expr[i] == 'k') {
			result = mult(result, K);
		}
	}
	return result;
}

int main(int argc, char const *argv[])
{
	std::string endline;
	int N;
	std::cin >> N;
	getline(std::cin, endline);

	for (int testCase = 0; testCase < N; testCase++) {
		std::cerr << testCase << std::endl;
		std::string output = "NO";

		int L;
		std::cin >> L;
		long X;
		std::cin >> X;
		std::string line;
		getline(std::cin, line);
		getline(std::cin, line);

		std::string s = line;
		for (int i = 1; i < (X >= X%4+16 ? X%4+16 : X); i++) {
			s += line;
		}

		// std::cerr << s << std::endl;

		// std::cerr << line << std::endl;

		int* intervalQuat = evaluate(line);

		int* result = A;
		for (int i = 0; i < X%4; i++) {
			int* newResult = mult(result, intervalQuat);
			// if (i > 0) delete[] result;
			result = newResult;
			// std::cerr<<result[0]<<" "<<result[1]<<" "<<result[2]<<" "<<result[3]<<std::endl;
		}
		if (result[0] == -1) {


			int iEnd = 0;
			int jEnd = 1;

			int* i = A;
			while (iEnd < s.length()-2) {
				// std::cerr << iEnd << std::endl;
				int* nextQuat;
				if (s[iEnd] == 'i') {
					nextQuat = I;
				} else if (s[iEnd] == 'j') {
					nextQuat = J;
				} else if (s[iEnd] == 'k') {
					nextQuat = K;
				} else {
					std::cerr<<"FAIL"<<std::endl;
					return 0;
				}
				int* newI = mult(i, nextQuat);
				// if (iEnd > 0) delete[] i;
				i = newI;

				// std::cerr<<"I96: "<<i[0]<<" "<<i[1]<<" "<<i[2]<<" "<<i[3]<<std::endl;
				if (i[1] != 1) {
					iEnd++;
					continue;
				}

				int* j = A;
				int jEnd = iEnd+1;
				while (jEnd < s.length()-1) {
					// std::cerr<<"J:"<<jEnd<<std::endl;
					int* nextQuat;
					if (s[jEnd] == 'i') {
						nextQuat = I;
					} else if (s[jEnd] == 'j') {
						nextQuat = J;
					} else if (s[jEnd] == 'k') {
						nextQuat = K;
					} else {
						std::cerr<<"FAIL"<<std::endl;
						return 0;
					}
					int* newJ = mult(j, nextQuat);
					// if (jEnd > 0) delete[] j;
					j = newJ;

					// std::cerr<<"J118: "<<j[0]<<" "<<j[1]<<" "<<j[2]<<" "<<j[3]<<std::endl;
					if (j[2] != 1) {
						jEnd++;
						continue;
					}

					int* k = A;
					// std::cerr<<A[0]<<A[1]<<A[2]<<A[3]<<std::endl;
					for (int nextK = jEnd+1; nextK < s.length(); nextK++) {
						// std::cerr<<"K: "<<nextK<<std::endl;
						int* nextQuat;
						if (s[nextK] == 'i') {
							nextQuat = I;
						} else if (s[nextK] == 'j') {
							nextQuat = J;
						} else if (s[nextK] == 'k') {
							nextQuat = K;
						} else {
							std::cerr<<"FAIL"<<std::endl;
							return 0;
						}
						int* newK = mult(k, nextQuat);
						// if (nextK > 0) delete[] k;
						k = newK;
					}

					// std::cerr<<"K140: "<<k[0]<<" "<<k[1]<<" "<<k[2]<<" "<<k[3]<<std::endl;

					if (k[3] == 1) {
						output = "YES";
						goto endloop;
					}

					jEnd++;
				}

				iEnd++;
			}
		}
		endloop:

		printf("Case #%d: %s\n", testCase + 1, output.c_str());
	}
	return 0;
}
