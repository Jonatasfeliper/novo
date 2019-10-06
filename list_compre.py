#list comprehensions  = combina laços for e criação de novos elementos e concatena cada novo elemento automaticamente
lista = [valores**2 for valores in range(1,6,2)] #resultado de valores exponenciais de 1= 1,2 = 4= 16, 5=25 da lsta (#quadrados perfeitos))
print(lista)

#lista_cubo = [valores_cubo**3 for valores_cubo in range(1,9,3)] #resultado de valores exponenciais de 1= 1,2 = 4= 16, 5=25 da lsta (#quadrados perfeitos))
#print(lista_cubo)
#Numerospares = [valores_pares for valores_pares in range(0,1000001,2)] #resultado de valores exponenciais de 1= 1,2 = 4= 16, 5=25 da lsta (#quadrados perfeitos))
#print("Os números impares de 0 à 1Mi são:", Numerospares) #números pares de 0 à 1Mi
#print("A soma de numeros pares de 0 a 1Mi = ", sum(Numerospares)) #sama de numeros pares de 1 Mi


jogadores = ['Jonatas','Augusto','Gui','Maria']
print(jogadores[1:3]) #apresenta os jogadores de 1 à 3
print(jogadores[:3]) #apresenta os jogadores até 3
print(jogadores[3:]) #apresenta os jogadores apartir 3

listajogadores = jogadores[:] #cópia de listajogadores
jogador1 = 'Joao'
listajogadores.append(jogador1)

print(jogador1,'foi adicionado ao lista de jogadores: ',','.join(listajogadores))
print(listajogadores)
#podendo separar,quebrando em espaços com split

#print('{} foi adicionado a {:}'.format(jogador1, listajogadores)
#)
#print(jogador1,'foi adicionado a lista',*listajogadores, sep=" ") #sem os colchetes [aparentemente melhor forma]
#pag 101
