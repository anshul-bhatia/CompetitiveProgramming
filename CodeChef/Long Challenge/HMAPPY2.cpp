#define ll long long
#include<bits/stdc++.h>
using namespace std;
ll gcd(ll a,ll b)
{
  if(b==0)
    return a;
  else
  return gcd(b,a%b);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        unsigned ll n,k,a,b,count=0,c,d,an,e,bn,cn,g,lcm;
        cin>>n>>a>>b>>k;
        g=gcd(a,b);
        an=n/a;
        bn=n/b;
        lcm=(a*b)/g;
        cn=n/lcm;
        count=an+bn-2*cn;
        if(count>=k)
            cout<<"Win\n";
        else
            cout<<"Lose\n";
    }
}
