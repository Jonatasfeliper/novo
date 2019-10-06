
#print ("começo "); #pode ser com aspas duplas
#print ('começo de novo'); #ou aspas simples


#name =  "jônatas felipe "; #usando uma váriavel no nome podemos colocar o método title e iniciar com a letra maiúscula
#print (name.title()) #resultado Jônatas
#print (name.upper()) #ou usando upper transforma todas em maiúscula
#print (name.lower()) #ou todos em minúscula #lower

#sobrenome= "regis bernardo"
#nome_completo = name +"" + sobrenome
#print ("Olá, " + nome_completo.title()) #pode-ser fazer concatenações com +
#mensagem_completa = ("Olá, " + nome_completo)
#print(mensagem_completa.title()) #ou simplificar usando uma variável deixando assim apenas uma mensagem

#print("Languages:\n\tPython\n\tC\n\tJavaScript") #parei aqui pag 58s
nome = input("Digite seu nome: ") #input recebe dados pelo promp
sobrenome =  input("Digite seu sobrenome: ") #input de dados do sobrenome
nome_completo = nome + " " + sobrenome

print("Olá, bom dia " + nome_completo.title()) #podendo fazer concatenação com os dados recebidos
#data_Nascimento = input("Digite sua data de nascimento: ")

#print("Nome Completo: " + nome_completo + "\nData de Nascimento: " + data_Nascimento) #concatenação mais input e prints

#ling_favorit = input("Qual sua linguagem de programação? ")
#ling_favorit.rstrip() #remove espaços em branco termporariamente
#ling_favorit = ling_favorit.lstrip() #alterado diretamente na variável (permanentemente)
#ling_favorit.lstring #remove espaços antes
#ling_favorit.strip #remove espaços antes e depois
#print("Sua linguagem de programação favorita é python: " + ling_favorit.strip()) #remove espaços antes e depois #cuidado com as aspas simples quando usar apóstafos"'"

citacao_Biblia = '"Amaram mais as trevas que a luz"' #na sitação é bom usar aspas simples
autor = "joão" #com title colocamos a letra em maiúsculo

print(citacao_Biblia + " \n \t\t\t\t\t\t\t\t\t\tAutor: \t" + autor.title())


#numeros no python
soma = 2 + 3
sub = 3 - 2
mult = 3*2
div = 3/2

expoent = 3**3 #para expoente usa-se duas multiplicações
ordem_operac = 2+3*4 #ordem de operação
ordem_operac2 = (2+3)*4

print("resultado: ", + soma,mult,div,sub,expoent,ordem_operac,ordem_operac2) #soma = + porém para concatenar precisa na vírgula
 #ponto futluante : exemplo: 0.30000000000000004 (podemos remover excessos que casar decimais.)
 print  "Happy " + age + "rd Birthday!"
