#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    long int L[100000],R[100000],P[100000],i,j,k;
    int N,M,T;//,count=0,i;
    cin>>T;
    for(j=0;j<T;j++)
    {
        cin>>N>>M;
        for(i=0;i<N;i++)
        {
            cin>>L[i]>>R[i];
        }
        for(i=0;i<M;i++)
        {
            cin>>P[i];
        }
        for(i=0;i<N;i++)
            {
                for(k=0;k<N-i;k++)
                {
                    if(L[k]>L[k+1])
                    {
                        int temp=L[k];
                        int temp1=R[k];
                        L[k]=L[k+1];
                        R[k]=R[k+1];
                        L[k+1]=temp;
                        R[k+1]=temp1;
                    }
                }
            }
        for(i=0;i<M;i++)
        {
            if(P[i]>R[N])
               {
                P[i]=-1;
                continue;
               }
            if(P[i]<L[0])
                {
                    P[i]=L[0]-P[i];
                    continue;
                }
            for(k=0;k<N;k++)
            {
                if(P[i]>=L[k]&&P[i]<R[k])
                {
                    P[i]=0;
                    break;
                }
                if(P[i]==R[k])
                {
                    P[i]=L[k+1]-P[i];
                    break;
                }
                if(P[i]>R[k] && P[i]<L[k+1])
                 {
                     P[i]=L[k+1]-P[i];
                     break;
                 }
            }
        }

        for(int i=0;i<M;i++)
        {
            cout<<P[i]<<endl;
        }
    cout<<endl;
    }
return 0;
}
