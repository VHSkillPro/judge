#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    vector<int> a(n);
    for (auto &i: a) cin >> i;
    cout << accumulate(a.begin(), a.end(), 0);
    return 0;
}