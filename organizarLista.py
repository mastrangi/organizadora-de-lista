import time

lista = []
lista_crescente = []

def to_lista_crescente(contador):
    for num in lista:
        if contador == 0:
            lista_crescente.insert(contador, num)
            contador = contador + 1
        else:
            for itens in lista_crescente:
                if num < itens: 
                    lista_crescente.insert(lista_crescente.index(itens), num)
                    contador = contador + 1
                    break
            else:
                lista_crescente.append(num)

while True:
    numero = input("(DIGITE 'FIM' PARA ORGANIZAR)!!!! \nDigite um número que quer adicionar a lista para organizar: ")
    
    if numero.lower() == 'fim':
        print("OBSERVE A SUA LISTA ORGANIZADA")
        time.sleep(1.5)
        to_lista_crescente(0)
        break
    elif numero.isdigit():
        lista.append(numero)
        print("Essa é sua lista atualizada: ", lista)
        time.sleep(1.5)
    else:
        print("DIGITE UM NÚMERO OU FIM!!!!!!!!!!!")    
        time.sleep(1.5)

lista_decrescente = lista_crescente[::-1]
print("Lista crescente: ", lista_crescente)
print("Lista decrescente: ", lista_decrescente)