v = list(map(int, input().split()))

if v[0]%v[1]==0 or v[1]%v[0]==0:
    print('Sao multiplos')
else:
    print('Nao sao multiplos')