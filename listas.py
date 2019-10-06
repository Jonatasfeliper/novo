#listas python

nomes = ["joão","Mateus","Ricardo"," juarez "] #criação de listas

#funções

print(nomes[0].title().strip()) # ver apenas o arquivo da posição da lista
print(nomes[1].title().strip()) #posso reformular usando title que saira em letras maiúsculas
print(nomes[2].title().strip())
print(nomes[3].strip().title()) # remover estaços em branco também.


#métodos
print(nomes[-1].strip().title()) #penúltimo item da lista
nomes.append('Igor')
Mensagem = ("Nomes inseridos na lista: " + nomes[-1]) #podendo adicionar itens na lista
print (Mensagem)
nomes.append('Marcos')
Mensagem = ("Nomes inseridos na lista: " + nomes[-1]) #podendo adicionar itens na lista
print(Mensagem)
nomes[1]=('Guilherme') ##fazendo alterações na lista
print("Lista completa: " ,nomes)
nomes.insert(3,'Jonatas')
print("Lista completa: " ,nomes) #(colocando usuários em qualquer posição)
del nomes[1]
print("Lista completa: " ,nomes) #(removendo)

popped_nomes= nomes.pop(2)   #removendo e armazenando um arquivo em uma variável para ser usado depois
print(nomes)
print( "Nome removido: ", popped_nomes)
nomes.insert(4,popped_nomes) #usando a variável que contém o arquivo removido para readicionar
print(nomes)

nomes.remove('joão') #removendo itém de acordo com valor
#itens_removido1 = 'Igor' #porém parece que esse método está recebendo apenas leitura e não mais variável
#nomes.remove = (itens_removido1)
#print(nomes)
#print(itens_removido1)

nomes.append(' fred')

print (nomes)
nomes =[i.strip().title() for i in nomes]

nomes.sort()#coloca as infomações em ordem alfabetica
print (nomes)

nomes.sort(reverse=True)#ordem inverse ao alfabeto
print(nomes)

print(sorted(nomes))#permite exibir sua lista em uma ordem em particular
print(nomes) #método reverse pode ser usado pra mudar a ordem de lista para o contrário
nomes.append("joao")
print(nomes)
nomes =[i.strip().title() for i in nomes]
nomes.sort()
print (nomes)
len(nomes) #colocando quantidade de itens na lista
quantidade_nomes =len(nomes)
print("Sua lista tem: ", quantidade_nomes, " itens.")

nomes.append("joao")

nomes =[i.strip().title() for i in nomes]
nomes.sort()
print(nomes)

len(nomes) #colocando quantidade de itens na lista
quantidade_nomes =len(nomes)
print("Sua lista tem: ", quantidade_nomes, " itens.")



#pag 94
