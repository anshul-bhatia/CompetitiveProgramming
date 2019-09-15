#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int S[100],J[100];
    int N,T,count=0,i;
    cin>>T;
    for(int j=0;j<T;j++)
    {
        count=0;
        cin>>N;
        for(i=0;i<N;i++)
        {
            scanf("%d %d",&S[i],&J[i]);
            if(J[i]-S[i]>5)
                count++;
        }
        cout<<count<<endl;
    }
}
