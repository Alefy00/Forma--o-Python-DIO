class Bicicleta:
    def __init__(self, cor, modelo, ano,  valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("bibipi")
    
    def parar(self):
        print("parando bicicleta")
        
    def correr(self):
        print("correndo")
        
    


b1 = Bicicleta("branca", "monark", 2024, 500)

b1.buzinar()
b1.parar()
b1.correr()  


      