#Tupla
paises = ('Brasil', 'Paraguai', 'França', 'Portugal', 'Suiça', 'China', 'EUA', 'Japão', 'Republica Tcheca', 'Itália')

#exibir tupla
for pais in paises:
    print(pais)

#Exibe o tipo de coleção
print('\n')
print(type(paises))
print('\n')

#joga a tupla em uma lista e ordena
paises_lista = sorted(paises)

#exibe a lista
for pais in paises_lista:
    print(pais)

print('\n')
print(type(paises_lista))
    