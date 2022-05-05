def remove_dupes(lista):
	return [x for x in lista if lista.count(x) == 1]

lista_testes = [1,2,3,3,4,5,6,6,7,8,9,9,9,10]

print(remove_dupes(lista_testes))