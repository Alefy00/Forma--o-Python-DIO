class Animal:
    def __init__(self, patas) -> None:
        self.patas = patas
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {' '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        
    

class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Cachorro(Mamifero):
    pass


class Onitorrinco(Mamifero,Ave):
    pass


#og = Cachorro(4, "branco")
#print(dog)

oni = Onitorrinco(cor_pelo="branca", patas=2,cor_bico="red")
print(oni)