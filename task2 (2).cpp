#include<bits/stdc++.h>

using namespace std;

void task2(){
    string f;
    cin>>f;
    int out,k,m=f.size();
    cin>>out>>k;
    int p=1<<k;

    for(int i=0;i<m;++i){
        if(i%p/(p/2)==out){
            cout<<f[i];
        }
    }
}
int main(){
    task2();
}
