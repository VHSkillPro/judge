#include <bits/stdc++.h>
using namespace std;

const long long mod = 1e9+7;

int main(){
    int n; cin >> n;
    // cout << (n + 1) * n / 2 % mod;
    long long sum = 0;
    for (long long i = 1; i <= n; i++) {
        sum = (sum + i) % mod;
    }
    cout << sum;
    return 0;
}