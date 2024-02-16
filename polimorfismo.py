class Passaro:
    def voar(self):
        pass

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")
        

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")
        

def plano_de_voo(passoro):
    passoro.voar()
    
    
plano_de_voo(Pardal())
plano_de_voo(Avestruz())