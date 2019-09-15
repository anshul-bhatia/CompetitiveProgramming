#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t,i,j,k;
  cin>>t;
  while(t--)
  {
    int D,Q,d[31],p[31],dead[100],req[100];
    cin>>D;
    for(i=0;i<D;i++)
    {
      cin>>d[i]>>p[i];
    }
    cin>>Q;
    for(i=0;i<Q;i++)
    {
      cin>>dead[i]>>req[i];
      int sum=0,j=0;
      for(k=0;k<D;k++)
      {
        if(d[k]<=dead[i])
          sum=sum+p[k];
      }
      if(sum<req[i])
        cout<<"Go Sleep\n";
      else
        cout<<"Go Camp\n";
    }
  }


  }
