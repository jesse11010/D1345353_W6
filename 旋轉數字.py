x = input('輸入：')
r = list(x)
m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
for c in r:
    if c in ['2', '3', '4', '5', '7']:
        print('false')
        break
else:
    m = ''.join(m[c] for c in r)
    print(m)