#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
#define accuracy chrono::steady_clock::now().time_since_epoch().count()
mt19937 rnd(accuracy);

ull random(ull l, ull r) {
    return rnd() % (r - l + 1) + l;
}

int main(int argc, char* argv[]){
    int n = random(1000, 10000);
    cout << n << "\n";

    for (int i = 1; i <= n; i++) 
        cout << random(ull(1), ull(1e5)) << " ";

    return 0;
}