/*
 * Aaron Miller
 * Google Code Jam 2015
 */
#include <iostream>
#include <stdio.h>

bool solveI(int, int*, std::string);
bool checkJ(int, int*, int, int, std::string);
bool solveK(int, int*, int, std::string);

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

bool solveI(int X, int* intervalQuat, std::string interval)
{
	std::cerr << X << std::endl;
	int* iResult = A;
	for (int i = 0; i < interval.length(); i++) {
		// std::cerr << i << std::endl;
		int* nextQuat;
		if (interval[i] == 'i') {
			nextQuat = I;
		} else if (interval[i] == 'j') {
			nextQuat = J;
		} else if (interval[i] == 'k') {
			nextQuat = K;
		}
		int* newIResult = mult(iResult, nextQuat);
		// if (i > 0) delete[] iResult;
		iResult = newIResult;

		std::cerr << "I"<<iResult[0]<<" "<<iResult[1]<<" "<<iResult[2]<<" "<<iResult[3]<<std::endl;

		if (i == interval.length()-1) {
			X--;
		}
		if (iResult[1] == 1) {
			// this works for i for nf == 0
			int* result = A;
			for (int j = i+1; j < interval.length(); j++) {
				int* nextQuat;
				if (interval[j] == 'i') {
					nextQuat = I;
				} else if (interval[j] == 'j') {
					nextQuat = J;
				} else if (interval[j] == 'k') {
					nextQuat = K;
				}
				int* newResult = mult(result, nextQuat);
				// if (result != A) delete[] result;
				result = newResult;
			}
			for (int j = 0; j < (X+1)%4; j++) {
				int* newResult = mult(result, intervalQuat);
				// if (result != A) delete[] result;
				result = newResult;
			}
			// std::cerr<<"result:"<<result[0]<<" "<<result[1]<<" "<<result[2]<<" "<<result[3]<<std::endl;
			if (result[1] == 1 && solveK(X, intervalQuat, (i+1)%(interval.length()), interval)) {
				// if (iResult != A) delete[] iResult;
				return true;
			}
		} else {
			int* quat1 = mult(intervalQuat, iResult);
			if (quat1[1] == 1 && X>=1) {
				// this works for i for nf == 1
				int* result = A;
				for (int j = i+1; j < interval.length(); j++) {
					int* nextQuat;
					if (interval[j] == 'i') {
						nextQuat = I;
					} else if (interval[j] == 'j') {
						nextQuat = J;
					} else if (interval[j] == 'k') {
						nextQuat = K;
					}
					int* newResult = mult(result, nextQuat);
					// if (result != A) delete[] result;
					result = newResult;
				}
				for (int j = 0; j < (X)%4; j++) {
					int* newResult = mult(result, intervalQuat);
					// if (result != A) delete[] result;
					result = newResult;
				}
				if (result[1] == 1 && solveK(X-1, intervalQuat, (i+1)%(interval.length()), interval)) {
					// delete[] quat1;
					// if (iResult != A) delete[] iResult;
					return true;
				}
			} else {
				int* quat2 = mult(intervalQuat, quat1);
				if (quat2[1] == 1 && X>=2) {
					// this works for i for nf == 2
					int* result = A;
					for (int j = i+1; j < interval.length(); j++) {
						int* nextQuat;
						if (interval[j] == 'i') {
							nextQuat = I;
						} else if (interval[j] == 'j') {
							nextQuat = J;
						} else if (interval[j] == 'k') {
							nextQuat = K;
						}
						int* newResult = mult(result, nextQuat);
						// if (result != A) delete[] result;
						result = newResult;
					}
					for (int j = 0; j < (X+3)%4; j++) {
						int* newResult = mult(result, intervalQuat);
						// if (result != A) delete[] result;
						result = newResult;
					}
					if (result[1] == 1 && solveK(X-2, intervalQuat, (i+1)%(interval.length()), interval)) {
						// delete[] quat2;
						// delete[] quat1;
						// if (iResult != A) delete[] iResult;
						return true;
					}
				} else {
					int* quat3 = mult(intervalQuat, quat2);
					if (quat3[1] == 1 && X>=3) {
						// this works for i for nf == 3
						int* result = A;
						for (int j = i+1; j < interval.length(); j++) {
							int* nextQuat;
							if (interval[j] == 'i') {
								nextQuat = I;
							} else if (interval[j] == 'j') {
								nextQuat = J;
							} else if (interval[j] == 'k') {
								nextQuat = K;
							}
							int* newResult = mult(result, nextQuat);
							// if (result != A) delete[] result;
							result = newResult;
						}
						for (int j = 0; j < (X+2)%4; j++) {
							int* newResult = mult(result, intervalQuat);
							// if (result != A) delete[] result;
							result = newResult;
						}
						if (result[1] == 1 && solveK(X-3, intervalQuat, (i+1)%(interval.length()), interval)) {
							// delete[] quat3;
							// delete[] quat2;
							// delete[] quat1;
							// if (iResult != A) delete[] iResult;
							return true;
						}
					}
					// delete[] quat3;
				}
				// delete[] quat2;
			}
			// delete[] quat1;
		}
	}
	// if (iResult != A) delete[] iResult;
	return false;
}

bool checkJ(int X, int* intervalQuat, int jStartIndex, int jEndIndex, std::string interval)
{
	// std::cerr << X << " " << jStartIndex << " " << jEndIndex << std::endl;
	if (jStartIndex <= jEndIndex && (X+4)%4 == 3) {
		// try doing it with nm == 0
		int* result = A;
		for (int i = jStartIndex; i <= jEndIndex; i++) {
			int* nextQuat;
			if (interval[i] == 'i') {
				nextQuat = I;
			} else if (interval[i] == 'j') {
				nextQuat = J;
			} else if (interval[i] == 'k') {
				nextQuat = K;
			}
			int* newResult = mult(result, nextQuat);
			// if (result != A) delete[] result;
			result = newResult;
		}
		// std::cerr << "J"<<result[0]<<" "<<result[1]<<" "<<result[2]<<" "<<result[3]<<std::endl;
		if (result[2] == 1) {
			// if (result != A) delete[] result;
			return true;
		}
		// if (result != A) delete[] result;
	}

	int* frontResult = A;
	// std::cerr << "J"<<A[0]<<" "<<A[1]<<" "<<A[2]<<" "<<A[3]<<std::endl;
	for (int i = jStartIndex; i < interval.length(); i++) {
		// std::cerr << "J"<<frontResult[0]<<" "<<frontResult[1]<<" "<<frontResult[2]<<" "<<frontResult[3]<<std::endl;
		int* nextQuat;
		if (interval[i] == 'i') {
			nextQuat = I;
		} else if (interval[i] == 'j') {
			nextQuat = J;
		} else if (interval[i] == 'k') {
			nextQuat = K;
		}
		int* newFrontResult = mult(frontResult, nextQuat);
		// if (frontResult != A) delete[] frontResult;
		frontResult = newFrontResult;
	}

	int* rearResult = A;
	for (int i = 0; i <= jEndIndex; i++) {
		int* nextQuat;
		if (interval[i] == 'i') {
			nextQuat = I;
		} else if (interval[i] == 'j') {
			nextQuat = J;
		} else if (interval[i] == 'k') {
			nextQuat = K;
		}
		int* newRearResult = mult(rearResult, nextQuat);
		// if (rearResult != A) delete[] rearResult;
		rearResult = newRearResult;
	}
	// std::cerr << "J"<<frontResult[0]<<" "<<frontResult[1]<<" "<<frontResult[2]<<" "<<frontResult[3]<<std::endl;
	// std::cerr << "J"<<rearResult[0]<<" "<<rearResult[1]<<" "<<rearResult[2]<<" "<<rearResult[3]<<std::endl;

	int* quat1 = mult(frontResult, rearResult);
	if (quat1[2] == 1 && X%4 == 0) {
		// delete[] quat1;
		// if (frontResult != A) delete[] frontResult;
		// if (rearResult != A) delete[] rearResult;
		return true;
	}
	quat1 = mult(mult(frontResult, intervalQuat), rearResult);
	if (quat1[2] == 1 && X%4 == 1) {
		// delete[] quat1;
		// if (frontResult != A) delete[] frontResult;
		// if (rearResult != A) delete[] rearResult;
		return true;
	}
	quat1 = mult(mult(mult(frontResult, intervalQuat), intervalQuat), rearResult);
	if (quat1[2] == 1 && X%4 == 2) {
		// delete[] quat1;
		// if (frontResult != A) delete[] frontResult;
		// if (rearResult != A) delete[] rearResult;
		return true;
	}
	quat1 = mult(mult(mult(mult(frontResult, intervalQuat), intervalQuat), intervalQuat), rearResult);
	if (quat1[2] == 1 && X%4 == 3) {
		// delete[] quat1;
		// if (frontResult != A) delete[] frontResult;
		// if (rearResult != A) delete[] rearResult;
		return true;
	}
	
	// delete[] quat1;
	// if (frontResult != A) delete[] frontResult;
	// if (rearResult != A) delete[] rearResult;
	return false;
}

bool solveK(int X, int* intervalQuat, int jStartIndex, std::string interval)
{
	// std::cerr << X << " " << jStartIndex << std::endl;
	int* iResult = A;
	for (int i = interval.length()-1; i >= 0; i--) {
		// std::cerr << "\t" << i << std::endl;
		int* nextQuat;
		if (interval[i] == 'i') {
			nextQuat = I;
		} else if (interval[i] == 'j') {
			nextQuat = J;
		} else if (interval[i] == 'k') {
			nextQuat = K;
		}
		int* newIResult = mult(nextQuat, iResult);
		// if (iResult != A) delete[] iResult;
		iResult = newIResult;

		// std::cerr << "K"<<iResult[0]<<" "<<iResult[1]<<" "<<iResult[2]<<" "<<iResult[3]<<std::endl;

		if (i == 0) {
			X--;
		}
		if (iResult[3] == 1) {
			// this works for k for nr == 0
			if (checkJ(X, intervalQuat, jStartIndex, (i+interval.length()-1)%interval.length(), interval)) {
				return true;
			}
		} else {
			int* quat1 = mult(iResult, intervalQuat);
			if (quat1[3] == 1 && X>=1) {
				// this works for k for nr == 1
				if (checkJ(X-1, intervalQuat, jStartIndex, (i+interval.length()-1)%interval.length(), interval)) {
					return true;
				}
			} else {
				int* quat2 = mult(quat1, intervalQuat);
				if (quat2[3] == 1 && X>=2) {
					// this works for k for nr == 2
					if (checkJ(X-2, intervalQuat, jStartIndex, (i+interval.length()-1)%interval.length(), interval)) {
						return true;
					}
				} else if (mult(quat2, intervalQuat)[3] == 1 && X>=3) {
					// this works for k for nr == 3
					if (checkJ(X-3, intervalQuat, jStartIndex, (i+interval.length()-1)%interval.length(), interval)) {
						return true;
					}
				}
			}
		}
	}
	return false;
}

int main(int argc, char const *argv[])
{
	std::string endline;
	int N;
	std::cin >> N;
	getline(std::cin, endline);

	for (int i = 0; i < N; i++) {
		std::string output = "NO";

		int L;
		std::cin >> L;
		int X;
		std::cin >> X;
		std::string line;
		getline(std::cin, line);
		getline(std::cin, line);

		// std::cerr << line << std::endl;
		int* intervalQuat = evaluate(line);

		int* result = A;
		for (int i = 0; i < X%4; i++) {
			int* newResult = mult(result, intervalQuat);
			// if (i > 0) delete[] result;
			result = newResult;
			// std::cerr<<result[0]<<" "<<result[1]<<" "<<result[2]<<" "<<result[3]<<std::endl;
		}
		if (result[0] == -1 && solveI((X-2)%12, intervalQuat, line)) {
			output = "YES";
		}

		printf("Case #%d: %s\n", i + 1, output.c_str());
	}
	return 0;
}
