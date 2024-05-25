def adicionar_dado():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    
    return nome, cpf, telefone, email

def exibir_dados(nome, cpf, telefone, email):
    print("\nDados adicionados:")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")
    
nome, cpf, telefone, email = adicionar_dado()


exibir_dados(nome, cpf, telefone, email)
 


