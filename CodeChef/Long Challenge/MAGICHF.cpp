#include<iostream>
using namespace std;

int main()
{
  int T,N,X,S,A,B,contains,j;
  cin>>T;
  for(int i=0;i<T;i++)
  {
    cin>>N>>X>>S;
    int A[10000],B[10000];
    for( j=0;j<S;j++)
    {
      cin>>A[j]>>B[j];
    }
    if(A[0]==X)
    contains=A[0];
    else
    contains=B[0];
    for(j=0;j<S;j++)
    {
      if(A[i]==contains)
      {
        contains=B[i];
        continue;
      }
      else
      {
      contains=A[i];
      continue;
    }
    }
      cout<<contains;















  }
  return 0;
}
