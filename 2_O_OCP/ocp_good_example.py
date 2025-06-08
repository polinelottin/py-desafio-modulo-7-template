from abc import ABC, abstractmethod
'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

# Exemplo de uso:
class Exame(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def verificar_condicoes(self):
        pass

class ExameSangue(Exame):
    def __init__(self):
        super().__init__('sangue')
    
    def verificar_condicoes(self):
        if self.__verifica_condicoes_exame_sangue():
            print("Exame de sangue aprovado!")
        else:
            print("Exame de sangue não aprovado!")
    
    def __verifica_condicoes_exame_sangue(self):
        return True

class ExameRaioX(Exame):
    def __init__(self):
        super().__init__('raio-x')

    def verificar_condicoes(self):
        if self.__verifica_condicoes_exame_raio_x():
            print("Exame de raio-x aprovado!")
        else:
            print("Exame de raio-x não aprovado!")
  
    def __verifica_condicoes_exame_raio_x(self):
        return True

exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

exame_sangue.verificar_condicoes()
exame_raio_x.verificar_condicoes()


