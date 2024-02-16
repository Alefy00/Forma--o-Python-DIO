class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self) -> str:
        return f"{self.nome} ({self.numero}) - {self.escola}"
    
    

alefy = Estudante("Alefy", 21626)
nicole = Estudante("Nicole", 696969)

print(alefy)
print(nicole)