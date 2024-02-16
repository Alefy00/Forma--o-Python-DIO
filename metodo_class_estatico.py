class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def criar_data(cls, ano, mes, dia, nome):
        
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior(idade):
        return idade >= 18
    
        
    
#p = Pessoa("Alefy", 25)

#print(p.nome, p.idade)

p1 = Pessoa.criar_data(1998, 12, 2, "Alefy")

print(p1.nome, p1.idade)

print(Pessoa.e_maior(8))
    