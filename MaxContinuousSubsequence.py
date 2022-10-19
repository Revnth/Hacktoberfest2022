for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    l=list(set(l))
    cnt=0
    ans=0
   
    l.sort()
    for i in range(len(l)-1):
        if(abs(l[i+1]-l[i])==1):
            cnt=cnt+1
        else:
            cnt=0
        ans=max(ans,cnt)
    print(ans+1)
