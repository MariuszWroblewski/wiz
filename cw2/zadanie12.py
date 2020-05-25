for i in range(1, 11, 1):
    if (len(str(i)) == 1):
        print('|  ' + str(i) + '  |', end='')
    else:
        print('|  ' + str(i) + ' |', end='')
    for j in range(1, 11, 1):
        liczba = int(i) * int(j)

        if len(str(liczba)) == 1:
            print('  ' + str(liczba) + '  |', end='')
        elif len(str(liczba)) == 2:
            print('  ' + str(liczba) + ' |', end='')
        else:
            print(' ' + str(liczba) + ' |', end='')
    print('')
