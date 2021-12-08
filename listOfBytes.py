def translate(n, t):
    listb = []
    for i in range(len(n)):
        x = n[i].encode('utf-8')
        listb.append(x)
    print(f'перевод в байт код {listb}')
    listS = []
    for i in range(len(t)):
        y = t[i].decode('utf-8')
        listS.append(y)
    print(f'перевод в строку {listS}')

a = ['привет', ',', 'как', 'у', 'тебя', 'дела', '?']
b = [b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82', b'\xd0\xba\xd0\xb0\xd0\xba', b'\xd1\x82\xd1\x8b']
c = translate(a, b)