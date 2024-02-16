def criar_usuario():
    
    if cpf != cpf:
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")
        
        return {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        }
    else:
      print("não é possivel criar um usuario com o mesmo cpf ")

# Lista para armazenar os usuários
usuarios = []

# Solicita a quantidade de usuários que deseja adicionar
quantidade_usuarios = int(input("Quantos usuários deseja adicionar? "))

# Adiciona cada usuário à lista
for _ in range(quantidade_usuarios):
    usuarios.append(criar_usuario())

# Exibe os usuários adicionados
print("\nUsuários adicionados:")
for usuario in usuarios:
    print(usuario)
