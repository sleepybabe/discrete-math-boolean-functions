#include<bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin>>n;
    int m = 1<<n;
    srand(time(0));
    vector<bool> f(m);
    for(int i=0;i<m;++i){
        f[i] = rand() % 2;
        cout<<f[i];
    }
}
