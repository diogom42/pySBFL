#include <stdio.h>
int main(int argc, char *argv[])
{
char s[1000001];
long long int a[10]={0},q=0,ans,num=10,i;
char c;
s[0]=getchar();

while((c=getchar())!='\n')
{
if(c>='A' && c<='J')a[c-'A']=1;
else if(c=='?')q++;
}

if(s[0]>='1' && s[0]<='9'){ans=1;}
else if(s[0]>='A' && s[0]<='Z'){ans=9;num=9;a[s[0]-'A']=0;}
else ans=9;

if(q>0)ans=ans*q*10;

for(i=0;i<10;i++)
{if(a[i]==1)ans*=num--;}

printf("%lld",ans);
return 0;
}
