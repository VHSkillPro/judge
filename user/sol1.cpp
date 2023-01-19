#include <bits/stdc++.h>
using namespace std;

const long long mod = 1e9+7;

int main(){
    long long n; cin >> n;
    if (n % 2 == 0) cout << (n / 2) % mod * (n + 1) % mod;
    else cout << ((n + 1) / 2) % mod * n % mod;
    return 0;
}