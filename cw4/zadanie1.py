a = [x for x in range(1,100) if x%4==0]
print(a)
plik=open('dane1.txt', 'a')
plik.writelines(str(a))
plik.close()