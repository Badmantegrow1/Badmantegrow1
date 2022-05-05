s = 'abcc'
a = 0
b = 0
c = 0
d = 0
list = []
for _ in s:
    if _ == 'a' and b == 0 and c == 0:
        a += 1
    else:
        if _ == 'b':
            b += 1
        else:
            if _ == 'c':
                c += 1
            else:
                if a != 0 and b != 0 or c != 0:
                    d += 1
if a != 0:
    a = f'a{a}'
    list.append(a)
if b != 0:
    b = f'b{b}'
    list.append(b)
if c != 0:
    c = f'c{c}'
    list.append(c)
if d != 0:
    d = f'a{d}'
    list.append(d)
for _ in list:
    print(_, end='')
