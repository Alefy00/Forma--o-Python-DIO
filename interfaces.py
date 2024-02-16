from abc import ABC, abstractmethod


class Controle(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        return "LG"


class ControleTV(Controle):
    
    def ligar(self):
        print("Ligando TV")
    
    def desligar(self):
        print("Desligando TV")
    
    

controle = ControleTV()

controle.ligar()
controle.desligar()
print(controle.marca())