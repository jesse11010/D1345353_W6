while True:
    op=input("選擇運算符號（+，-，*，/）： ").split()
    a=int(input('請輸⼊第⼀個數字：'))
    if a==-999:
        print('程式結束。')
        break
    b=int(input('請輸⼊第二個數字：'))
    if b==-999:
        print('程式結束。')
        break
    elif op =='+':  
        print(a,'+',b,'=',a+b)
    elif op =='-':
        print(a,'-',b,'=',a-b)
    elif op =='*':
        print(a,'*',b,'=',a*b)
    elif op=='/' and b==0:
        print('不能除以 0，請重新輸⼊。')
    elif op =='/':
        print(a,'/',b,'=',a/b)

