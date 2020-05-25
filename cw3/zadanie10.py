def zakupy(**produkty):
    x = 0
    for cos in produkty:
        print(cos," ilosc ",produkty[cos])
        x+=int(produkty[cos])
    print("w sumie kupisz ",x," sztuk produktow")


zakupy(jajka="10",mleko="3",banany="4")