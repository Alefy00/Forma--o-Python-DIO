class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Lingando motor")
        
    def __str__(self) -> str:
        return self.cor
        

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas,carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
        
           
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} Esta carregado")


moto = Moto("branca", "PUU-7490", 2)

moto.ligar_motor()

carro = Carro("vermelha", "PUU-7490", 4)
carro.ligar_motor()

caminhao = Caminhao("preta", "PUU-7490", 10, False)
caminhao.ligar_motor()

caminhao.esta_carregado()

print(carro)

