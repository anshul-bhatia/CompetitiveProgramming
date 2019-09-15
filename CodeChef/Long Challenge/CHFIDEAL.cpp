#include<bits/stdc++.h>
using namespace std;
int main()
{
  int x,y,z,arr[]={1,2,3};
  x=2;
  cout<<x<<endl;
  cin>>y;
  for(int i=0;i<3;i++)
  {
    if(arr[i]==y || arr[i]==x)
      continue;
    else
      z=arr[i];
  }
  fflush(stdout);
  cout<<z<<endl;
}
