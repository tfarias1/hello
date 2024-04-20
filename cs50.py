import os
os.system('cls')


"""Solicitando dados ao usuário e usanfo f-strings"""
print('"""Solicitando dados ao usuário e usanfo f-strings"""')

name = input('Informe seu nome: ')
print(f'Seja muito bem vindo, {name} \n')


#-----------------------------------------------------------------------------------------

"""Variáveis"""
a = 28 # intinger
b = 1.5 # float
c = 'hello' # string
d = True #T rue/False
e = None


#-----------------------------------------------------------------------------------------

"""Condições"""
n = int(input("Insira um número: "))
if n > 0:
    print(f'{n} é um numero positivo \n')
elif n < 0:
     print(f'{n} é um numero negativo \n')
else:
    print('Zero \n')


#-----------------------------------------------------------------------------------------

"""Sequencias"""
print(name[0] + '\n')



#-----------------------------------------------------------------------------------------


"""Listas - São sequências Mutáveis / Editáveis"""
nomes = ["Thiago", "Natalia", "Lucas", "Júlia", "Heitor", "Maylon", "Bolt"]
print(f'{nomes}')
print(f'Imprimindo no mome na posição nomes[0]: {nomes[0]} \n')

nomes.append("Sara")
print(f'Imprimindo lista de nomes depois do Append "Sara": {nomes} \n')

nomes.remove("Sara")
print(f'Imprimindo lista de nomes depois do Remove "Sara": {nomes} \n')


#-----------------------------------------------------------------------------------------

"""Sets - Lista que não permite repetição de dados"""
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(f'Imprimindo Sets: {s}')
print(f'O Set possui {len(s)} elementos')
s.remove(3)
print(f'Imprimindo Sets: {s} \n')


#-----------------------------------------------------------------------------------------

"""Tuplas - São sequências Imutáveis / Não Editáveis"""
cordenadas = (10.0, 20.0)
print(f'{cordenadas} \n')


#-----------------------------------------------------------------------------------------

"""Loopings"""
print("Loopins - For:")
for i in range(6):
    print(i)
print()


for nome in nomes:
    print(nome)
print()


#-----------------------------------------------------------------------------------------

"""Dicionários"""
print("Dicionários:")
casas = {'Harry': "Grifinória", 'Draco': 'São Serina'}
casas["Hermione"] = "Grifinória"
print(f'Harry: {casas["Harry"]}')
print(f'Hermione: {casas["Hermione"]} \n')


#-----------------------------------------------------------------------------------------

"""Funções"""
print("Funções:")

def quadrado(x):
    return x * x

for i in range(10):
    print(f'O quadrado de {i} é {quadrado(i)}')

print()


#-----------------------------------------------------------------------------------------

"""Classes | São modelos de objetos"""
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2, 8)
print(p.x)
print(p.y)
print()


class Voo():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiros = []
    

    def add_passageiro(self, nome):
        if not self.assentos_livres():
            return False
        self.passageiros.append(nome)
        return True


    def assentos_livres(self):
        return self.capacidade - len(self.passageiros)
    


voo = Voo(4)

pessoas = ["Thiago", "Natalia", "Julia", "Heitor", "Joao"]
for pessoa in pessoas:
    sucesso = voo.add_passageiro(pessoa)
    if sucesso:
        print(f"{pessoa} adicionado(a) ao voo com sucesso") 
    else:
        print(f"Não existem mais assentos disponíveis para {pessoa} neste voo")


print()


#-----------------------------------------------------------------------------------------

"""Decoretors"""

def anuncio(f):
    def involucro():
        print("Sobre como rodar funções...")
        f()
        print("Pronto com funções")
    
    return involucro

@anuncio
def ola():
    print("Olá")


ola()
