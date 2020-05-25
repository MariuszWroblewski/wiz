x = input("podaj liczbe mniejsza badz rowna 10:")
x=int(x)
wynik=""
if x>10:
    print("liczba wieksza od 10")

else:
    while(x>0):
        wynik=wynik+"A"
        print(wynik)
        x=x-1