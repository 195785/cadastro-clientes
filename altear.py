def encontrar_usuario_por_id(usuarios, id_usuario):
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            return usuario
    return None

def atualizar_telefone(usuarios, id_usuario, novo_telefone):
    usuario = encontrar_usuario_por_id(usuarios, id_usuario)
    if usuario:
        usuario['telefone'] = novo_telefone
        return True
    else:
        return False
    
usuarios = [
    {'id': 1, 'nome': 'João', 'telefone': '123456789'},
    {'id': 2, 'nome': 'Maria', 'telefone': '987654321'},
    {'id': 3, 'nome': 'Pedro', 'telefone': '555555555'}
]

id_usuario = 3
novo_telefone = '(11) 99568-9068'

if atualizar_telefone(usuarios, id_usuario, novo_telefone):
    print(f"Telefone do usuário {id_usuario} atualizado com sucesso!")
else:
    print(f"Usuário com ID {id_usuario} não encontrado.")