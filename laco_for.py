magicos =['Edu','maria', 'joana'] #lista de mágicos
for magico in magicos: #for passa em lista quantos arquivos de mágicos tem #i é o contador #magicos é o tanto de fez que será executado
    print(magico.title() + ",é o mágico da semana")  #print com nome dos mágicos
    print("Estamos ansiosos por ver seu trabalho, " + magico.title() + ".\n") #identificação  e boas vinda para cada mágico

print("Obrigado pela participação de todos vocês," + magicos[0].title(),",",magicos[1].title(),",",magicos[2].title())
