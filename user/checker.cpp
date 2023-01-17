#include <bits/stdc++.h>
using namespace std;

int main(int argc, char* argv[]){
    int n, m; cin >> n >> m;
    
    ifstream fout(argv[1]);
    ifstream fans(argv[2]);

    string out; fout >> out;
    string ans; fans >> ans;

    if (out != ans) {
        cout << "Wrong answer!!";
        return 1;
    }

    fout >> out;
    fans >> ans;

    auto get = [&](const string &str){
        int sum = 0;
        for (auto &ch: str) {
            if (ch == 'A') sum += 1;
            else if (ch == 'T' || ch == 'J' || ch == 'Q' || ch == 'K') sum += 10;
            else sum += (ch - '0');
        }
        return sum;
    };

    if (get(out) != get(ans)) {
        cout << "Wrong sum!!";
        return 1;
    }

    cout << "Accept!!";
    return 0;
}