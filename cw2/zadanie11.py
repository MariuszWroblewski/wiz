h = 0
while (h < 3 or h > 9):
    print('Wysokość ma być mniędzy <3,9>')
    h = int(input('Podaj wysokość: '))
h_parzysta = False
if (h % 2 == 0):
    h_parzysta = True
    h = h - 1
s = h // 2
kolo = 1
for i in range(0, h // 2, 1):
    for j in range(0, s, 1):
        print(' ', end='')
    s = s - 1
    for j in range(0, kolo, 1):
        print('O', end='')
    kolo = kolo + 2
    print()

for i in range(0, h, 1):
    print('O', end='')
print()
if (h_parzysta == True):
    for i in range(0, h, 1):
        print('O', end='')
    print()

s = 1
kolo = h - 2
for i in range(0, h // 2, 1):
    for j in range(0, s, 1):
        print(' ', end='')
    s = s + 1
    for j in range(kolo, 0, -1):
        print('O', end='')
    kolo = kolo - 2
    print()