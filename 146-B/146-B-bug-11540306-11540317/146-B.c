#include<stdio.h>
int main(int argc, char *argv[])
{
    char st[20],at[20];
    int a,b,q,p,d,v,i,e;
    scanf("%d%d",&a,&b);
    q=0;
    while(1)
    {
        st[q]=(b%10)+48;
        b=b/10;
        q++;
        if(b==0)
        break;
    }
    while(1)
    {
        d=a;
        p=0;
        while(1)
    {
        e=(d%10)+48;
        d=d/10;
        if(e=='4'||e=='7')
        {
            at[p]=e;
        p++;}
        if(d==0)
        break;
    }
    v=0;
    if(q==p)
    {
        for(i=0;i<p;i++)
        {
            if(st[i]==at[i]);
            else
            {
                v=1;
            }
        }
    }
    else
    v=1;
    if(v==0)
    break;
    a++;
    }
    printf("%d\n",a);
    return 0;
}