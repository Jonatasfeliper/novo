#testes python
assert 4 == 4 #não deu erro é igua 4
#assert 4<4 #4 não é menor que 4

def soma (x,y): #def cria uma função nova
    return x + y
assert soma(2, 2) == 2 + 2 #verdadeiro #assert afirma
assert soma(2,2) == 5 , '2  mais  2 é diferente  de 5'
