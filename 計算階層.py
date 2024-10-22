n=int(input('請輸⼊⼀個正整數：'))
total=1
if n>=0:
    if n==0:
        total=0
    else:
        for i in range(1,n+1):
            total*=i
            i+=1
    print(n,'!=',total)
else:
    print('請輸⼊⼀個有效的正整數。')

    