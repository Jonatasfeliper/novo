from unittest import TestCase ,main#importação de testes

def soma(x,y): #criar função soma
    return x + y #retorna valor de x e y

def sub(x,y):
    return x - y

def mult (x,y):
    return x * y

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(5,5),10)

if __name__ == '__main__':
    main()
