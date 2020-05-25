zakupy = {'jaja': 'sztuki','maslo': 'kostki', 'pieczywo': 'sztuki'}

lista=[x for (x,y) in zakupy.items() if y=='sztuki']
print(lista)