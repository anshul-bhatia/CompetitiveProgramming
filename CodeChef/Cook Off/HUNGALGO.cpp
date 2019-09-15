#include <iostream>
using namespace std;
#define ll long long
int main() {
	ll t;
	cin>>t;
	while(t--)
	{
	    ll n,i,j,countr=0,countc=0;
	    cin>>n;
	    ll arr[n][n];
	    for(i=0;i<n;i++)
	    {
	        for(j=0;j<n;j++)
	        {
	            cin>>arr[i][j];
	        }
	    }
	    int flag=0,flagc=0;
	    for(i=0;i<n;i++)
	    {
	        flag=0;
	        for(j=0;j<n;j++)
	        {
	            if (arr[i][j]==0)
	                flag=1;
	        }
	        if (flag==1)
	            countr++;
	    }
	    int flag1=0;
	    for(i=0;i<n;i++)
	    {
	        flag1=0;
	        for(j=0;j<n;j++)
	        {
	            if (arr[j][i]==0)
	                flag1=1;
	        }
	        if (flag1==1)
	            countc++;
	    }
	    if (countr==n && countc==n)
	        cout<<"YES\n";
	    else
	        cout<<"NO\n";
	}
	return 0;
}
