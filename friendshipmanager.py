'''
Módulo que contém funções associadas à gerência da parte social da plataforma.
'''
import database as db

def send_friend_request(sender: str, receiver: str):
    ''' Envia um pedido de amizade de um usuário para outro.
    
    Parâmetros:
    - sender: nome do usuário que enviou o pedido
    - receiver: nome do usuário para o qual o pedido será enviado
    
    Retornos:
    - 1: nomes de usuários são iguais
    - 2: usuário recebedor não encontrado
    - 3: pedido de amizade anterior pendente
    - 4: usuários já são amigos
    - 0: pedido enviado com sucesso '''
    if sender == receiver: return 1

    if not db.get_user_by_name(receiver): return 2

    friendship = db.get_friendship(sender, receiver)
    if friendship: return 3 if friendship[2] else 4

    friendship = db.get_friendship(receiver, sender)
    if friendship: return 3 if friendship[2] else 4

    db.insert_friendship_request(sender, receiver)
    return 0

def accept_friend_request(sender: str, receiver: str):
    ''' Aceita um pedido de amizade pendente.
    
    Parâmetros:
    - sender: nome do usuário que enviou o pedido
    - receiver: nome do usuário que recebeu o pedido
    
    Retornos:
    - 1: pedido de amizade não encontrado
    - 0: pedido aceito com sucesso '''
    if not db.get_friendship(sender, receiver): return 1

    db.accept_friendship_request(sender, receiver)
    return 0

def reject_friend_request(sender: str, receiver: str):
    ''' Rejeita um pedido de amizade pendente.
    
    Parâmetros:
    - sender: nome do usuário que enviou o pedido
    - receiver: nome do usuário que recebeu o pedido
    
    Retornos:
    - 1: pedido de amizade não encontrado
    - 0: pedido rejeitado com sucesso '''
    if not db.get_friendship(sender, receiver): return 1

    db.reject_friendship_request(sender, receiver)
    return 0

''' ------------------------------------------------------------------------ '''

''' Testes. '''
if __name__ == '__main__':
    import sys

    print(send_friend_request('a', 'a')) # mesmo nome
    print(send_friend_request('a', 'c')) # usuário recebedor inexistente
    print(send_friend_request('a', 'b')) # correto
    print(send_friend_request('a', 'b')) # pedido pendente
    print(reject_friend_request('a', 'b')) # correto
    print(reject_friend_request('a', 'b')) # pedido não encontrado
    print(accept_friend_request('a', 'b')) # pedido não encontrado
    print(send_friend_request('a', 'b')) # correto
    print(accept_friend_request('a', 'b')) # correto
    print(send_friend_request('a', 'b')) # já amigos

    sys.exit(0)
