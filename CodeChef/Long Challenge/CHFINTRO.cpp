#include<bits/stdc++.h>
using namespace std;
int main()
{
  int N,r;
  cin>>N>>r;
  for(int i=0;i<N;i++)
  {
    int c;
    cin>>c;
    if(c<r)
      cout<<"Bad boi\n";
    else
      cout<<"Good boi\n";
  }
}
