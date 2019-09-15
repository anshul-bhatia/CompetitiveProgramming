#include<bits/stdc++.h>
#include<math.h>
using namespace std;
int numerator(int n)
{
    if(n==0)
        return 0;
    if(n==1)
        return 1;
    return numerator(n-1)+2*numerator(n-2);

}
int main()
{
    int t,i;
    cin>>t;
    int n[t];
    for(i=0;i<t;i++)
    {
        cin>>n[i];
    }
    int y[t],x[t];
    for(i=0;i<t;i++)
    {

        x[i]=numerator(n[i]);
        y[i]=pow(2,n[i]);
    }
    for(i=0;i<t;i++)
    {
        cout<<x[i]<<" "<<y[i]<<" ";
    }
}

