x=input()
xl=list(x)
i=0
q=-1
while i<len(xl)/2 and xl[i]==xl[q]:
    i+=1
    q-=1
if i==len(xl)//2:
    print('true') 
elif len(xl)%2==1:
    if i-1==len(xl)//2:
        print('true')
    else:
        print('false')
else:
    print('false')