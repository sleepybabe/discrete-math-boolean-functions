#include<bits/stdc++.h>

using namespace std;

void task3(){
    string f0,f1;
    cin>>f0>>f1;
    int k,m=2*f0.size();
    cin>>k;
    int p=1<<k;

    for(int i=0, x=0, y=0 ;i<m;++i){
        if(i%p/(p/2)==0)
            {cout<<f0[x++];}
        if(i%p/(p/2)==1)
            {cout<<f1[y++];}
    }
}
int main(){
    task3();
}
