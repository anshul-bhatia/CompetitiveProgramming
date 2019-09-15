#define ll long long
#include<bits/stdc++.h>
using namespace std;
int main()
{
  ll t,N,P,modulo,i,answer1,answer2,answer3;
  cin>>t;
  while(t--)
  {
    cin>>N>>P;
    if(N==1)
    {
      cout<<(P)*(P)*(P)<<endl;
      continue;
    }
    if(N==2)
    cout<<(P)*(P)*(P)<<endl;
    else{
    i=N/2+1;
    modulo=N%i;
    answer1=(P-modulo)*(P-modulo);
    answer2=(P-N)*(P-modulo);
    answer3=(P-N)*(P-N);
    cout<<answer1+answer2+answer3<<endl;
  }
}
}
