#include <bits/stdc++.h>
using namespace std;

<<<<<<< HEAD
typedef long long ll;
typedef long double ld;

void Solve() {
    int n; cin >> n;
    vector<ll> a(n);
    for (auto &i: a) cin >> i;
    
    ld sum = 0;
    for (auto &x: a) {
        sum += log(x);
    }
    
    auto check = [&](ll base){
        return n * log(base) > sum;
    };
    
    ll l = 0, r = *max_element(a.begin(), a.end()) + 1;
    while (l + 1 < r) {
        ll m = (l + r) >> 1;
        if (check(m)) r = m;
        else l = m;
    }
    
    cout << r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    int nTest = 1;
    // cin >> nTest;
    while (nTest--) {
        Solve();
        if (nTest > 0) {
            cout << "\n";
        }
    }
=======
int main(){
    cout << "a";
>>>>>>> 4d447929a8208e68663e24312afcf880364c0dc0
    return 0;
}