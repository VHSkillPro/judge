#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]){
    double seed = stold(string(argv[1]));
    srand((long long)seed);

    long long l = 1e8, r = 15e8;
    cout << rand() % (r - l + 1) + l;
    return 0;
}