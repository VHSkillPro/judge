#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <queue>
#include <bitset>
#include <iomanip>
#include <fstream>
#include <stack>
using namespace std;

#define accuracy chrono::steady_clock::now().time_since_epoch().count()
mt19937 rng(accuracy);

vector<char> A = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', '*'};

int random(int l, int r) {
    return l + rand() % (r - l + 1); 
} 

int main(int argc, char* argv[]){
    srand(int(atof(argv[1])));
    
    int n = random(1, 10), m = random(1, 100);
    shuffle(A.begin(), A.end(), rng);

    cout << n << " " << m << endl;
    for (int i = 1; i <= n; i++) 
        cout << A[rand() % 14];
    return 0;
}