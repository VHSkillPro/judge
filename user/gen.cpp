#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]){
    srand(int(atof(argv[1])));
    int n = rand() % 100;
    cout << n << "\n";
    for (int i = 1; i <= n; i++)
        cout << rand() % 1000 << " ";
    return 0;
}