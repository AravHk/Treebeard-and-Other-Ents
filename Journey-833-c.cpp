#include <iostream>
#include <vector>
using namespace std;
#define ll long long
#define lld long double
#include <iomanip>

const ll template_array_size = 1e6+5460;
ll c[template_array_size];

int n;
ll ans = 0;
vector<ll> edges[100005];

lld dfs(ll cur,ll par){
    lld val = 0;
    ll nchild = 0;
    for(ll next:edges[cur]){
        if(next!=par){
            nchild++;
            val += dfs(next,cur);
        }
    }
    if(nchild==0){
        return 0;
    }
    return 1+val/nchild;
}

void solve(int tc=0){
    cin>>n;
    for(int i=0;i<n-1;i++){
        ll u,v;
        cin>>u>>v;
        --u;--v;
        edges[u].push_back(v);
        edges[v].push_back(u);
        
    }
    cout<<fixed<<setprecision(15)<<dfs(0,-1)<<"\n";
}
int main(){
    solve();
}
