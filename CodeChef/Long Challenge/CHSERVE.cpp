#include<iostream>
using namespace std;

int main()
{
    int t,i;
    cin>>t;
    long p1,p2,k,sum;
    for(i=0;i<t;i++)
    {
        cin>>p1>>p2>>k;
        sum=(p1+p2)%(2*k);
        if(sum<k)
            cout<<"CHEF";
        else
            cout<<"COOK";
        cout<<endl;
    }
}
