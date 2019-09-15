#include<bits/stdc++.h>
using namespace std;
int main()
{
  long long int t,N,a,b,i,countal,countbo,flag,countboth;
  cin>>t;
  while(t--)
  {
    flag=-1;
    countal=0;
    countbo=0;
    countboth=0;
    cin>>N>>a>>b;
    long long int n[N];
    for(i=0;i<N;i++)
    {
      cin>>n[i];
      if(n[i]%a==0 && n[i]%b!=0)
        countbo++;
      if(n[i]%b==0 && n[i]%a!=0)
        countal++;
      if(n[i]%a==0 && n[i]%b==0)
      countboth++;
    }
    if(countboth>0)
      countbo++;
    if(countal>=countbo)
      flag=0;
    else
      flag=1;
    if(flag==0)
      cout<<"ALICE\n";
    if(flag==1)
      cout<<"BOB\n";
  }
}
