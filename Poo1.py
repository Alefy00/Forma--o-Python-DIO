class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self ):
        print("Destruindo")
    
    def falar(self):
        print("auau")
        
     
        
    
c = Cachorro("livia", "branca")


c.falar()