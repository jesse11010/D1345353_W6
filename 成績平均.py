total = 0
i = 0
while True:
    x = input('請輸入成績：')    
    if x == '-1':
        if i == 0:
            print('沒有輸入任何成績')
        break
    elif not x.isdigit():
        print("請輸入有效的數字。")
        continue
    else:
        x = int(x)
        if x < 0:
            print('成績不能為負數，請重新輸入。')
            continue
        total+=x
        i+=1
if i != 0:
    print('平均成績為：',total / i)



 
    