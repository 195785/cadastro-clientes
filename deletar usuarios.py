{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cf4ccb2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Digite o nome do usuário a ser deletado: Maria\n",
      "Digite o CPF do usuário a ser deletado: 98765432100\n",
      "Digite o telefone do usuário a ser deletado: 987654321\n",
      "Usuário deletado com sucesso!\n"
     ]
    }
   ],
   "source": [
    "usuarios = [\n",
    "    {\"nome\": \"João\", \"cpf\": \"12345678900\", \"telefone\": \"123456789\"},\n",
    "    {\"nome\": \"Maria\", \"cpf\": \"98765432100\", \"telefone\": \"987654321\"}\n",
    "]\n",
    "\n",
    "def deletar_usuario(nome, cpf, telefone):\n",
    "    global usuarios\n",
    "    for usuario in usuarios:\n",
    "        if usuario['nome'] == nome and usuario['cpf'] == cpf and usuario['telefone'] == telefone:\n",
    "            usuarios.remove(usuario)\n",
    "            return True\n",
    "    return False\n",
    "\n",
    "# Exemplo de uso\n",
    "nome = input(\"Digite o nome do usuário a ser deletado: \")\n",
    "cpf = input(\"Digite o CPF do usuário a ser deletado: \")\n",
    "telefone = input(\"Digite o telefone do usuário a ser deletado: \")\n",
    "\n",
    "if deletar_usuario(nome, cpf, telefone):\n",
    "    print(\"Usuário deletado com sucesso!\")\n",
    "else:\n",
    "    print(\"Usuário não encontrado.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
