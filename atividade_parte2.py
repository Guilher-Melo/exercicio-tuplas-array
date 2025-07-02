# Parte 2: Dicionários
# 2.1 Crie um dicionário para um usuário. Use a chave 'username'
#  para o valor 'bia_costa', a chave 'email' para 'bia.costa@email.com',
#  e a chave 'data_adesao' para '2024-05-21'.

user = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'data_adesao': '2024-05-21'
}

# 2.2 Crie um dicionário para um produto. Use as chaves 'id_produto',
#  'nome', 'preco' e 'estoque' com os respectivos valores 'XYZ-001',
#  'Fone de Ouvido Sem Fio', 299.90 e 150.

produto = {
    'id_produto': 'XYZ-001',
    'nome': 'Fone de Ouvido Sem Fio',
    'preco': 299.90,
    'estoque': 150
}

# 2.3 Crie um dicionário vazio chamado preferencias_usuario.

preferencias_usuario = {}

# 2.4 Dado o dicionário de produto {'id_produto': 'XYZ-001',
#  'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150},
#  acesse e imprima o preço original.
#  Em seguida, atualize o preço para o valor promocional de 249.99.

print(produto['preco'])

produto['preco'] = 249.99

print(produto['preco'])

# 2.5 Dado o perfil de usuário {'username': 'bia_costa',
#  'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'},
#  adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.

user['telefone'] = '98765-4321'

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'},
#  use o método .get() para tentar acessar o valor da chave 'ultimo_login'.
#  Como a chave não existe, forneça o valor padrão 'Nunca logou'.
#  Após a tentativa, bia fez o login,
#  então atualize o dicionário para incluir
#  a chave 'ultimo_login' com o valor '2024-05-22'.

user.get('ultimo_login', 'Nunca logou')

user['ultmo_login'] = '2024-05-22'

# 2.7 Dado o perfil de usuário {'username': 'bia_costa',
#  'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'},
#  use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.

user_2 = {
    'username': 'bia_costa',
    'email': 'bia.costa@email.com',
    'telefone_fixo': '3265-4321'
}

user_2.pop('telefone_fixo')

print(user_2)

# 2.8 Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio',
#  'ABC-002': 'Teclado Mecânico'},
#  use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'
#  Armazene o valor retornado (o nome do produto)
#  e imprima uma mensagem de confirmação.

catalogo_produto = {
    'XYZ-001': 'Fone de Ouvido Sem Fio',
    'ABC-002': 'Teclado Mecânico'
}

produto_removido = catalogo_produto.pop('XYZ-001')

print(f'Produto {produto_removido} removido com sucesso!')

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'},
#  tente remover a chave 'email' usando o método .pop().
# Forneça o valor padrão 'Email não encontrado.' para evitar um erro.

user_3 = {'username': 'bia_costa'}

user_3.pop('email', 'Email não encontrado')

# 2.10 Dado o catálogo de produtos {'Fone de Ouvido': 249.99,
#  'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50},
#  itere sobre seus itens e imprima o nome
#  e o preço de cada um no formato 'Nome: R$Preço'.

catalogo_produto = {
    'Fone de Ouvido': 249.99,
    'Teclado Mecânico': 450.00,
    'Mouse Gamer': 120.50
}

for nome, preco in catalogo_produto.items():
    print(f'{nome}: R${preco}')

# 2.11 Dado a lista de compras da feira {'Tapioca': 18.99,
#  'Queijo Manteiga': 45.00, 'Ovos': 23.50},
#  itere sobre seus itens e
# imprima o nome e o preço de cada um no formato 'Nome: R$Preço'
#  e depois imprima o total.

compras_feira = {
    'Tapioca': 18.99,
    'Queijo Manteiga': 45.00,
    'Ovos': 23.50
}

for comida, preco in compras_feira.items():
    print(f'{comida}: R${preco}')

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'},
#  adicione uma nova chave 'endereco'. O valor associado a
# essa chave deve ser outro dicionário
# contendo: 'rua': 'Rua das Flores, 123',
#  'cidade': 'São Paulo' e 'cep': '01000-000'.

user_4 = {'username': 'bia_costa'}

user_4['endereco'] = {
    'rua': 'Rua das Flores, 123',
    'cidade': 'São Paulo',
    'cep': '01000-000'
}

# 2.13 Dado o perfil de usuário {'username': 'bia_costa'},
#  adicione uma nova chave 'profissao'.
#  O valor associado a essa chave deve ser outro dicionário
#  contendo: 'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'.

user['profissao'] = {
    'cargo': 'Desenvolvedora',
    'empresa': 'Tech Solutions'
}

# 2.14 A partir do perfil de usuário com endereço
# e profissão aninhados da questão anterior,
#  acesse e imprima apenas o valor associado à chave 'cidade'.

print(user_4['endereco']['cidade'])

# 2.15 Dado o perfil de usuário com endereço aninhado,
#  atualize o valor da chave 'rua' para 'Avenida Principal, 456'.

user_4['endereco']['rua'] = 'Avenida Principal, 456'

# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais.
#  Use a tupla (-8.0578, -34.8829) como chave para o valor 'Recife' e a
#  tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.

coordenada_recife = (-8.0578, -34.8829)
coordenada_sao_paulo = (-23.5505, -46.6333)

coordenadas = {
    coordenada_recife: 'Recife',
    coordenada_sao_paulo: 'São Paulo'
}

# 2.17 A partir do dicionário da questão anterior, adicione um novo local.
#  A chave deve ser a tupla (-22.9068, -43.1729)
#  e o valor deve ser 'Rio de Janeiro'.

coordenada_rio_de_janeiro = (-22.9068, -43.1729)

coordenadas[coordenada_rio_de_janeiro] = 'Rio de Janeiro'


# 2.18 Escreva uma função que, dado um dicionário de locais,
#  encontre o nome do local a partir de uma tupla de coordenadas.
#  A função deve retornar uma mensagem padrão caso a
# coordenada não seja encontrada.
#  Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).


def find_place(places: dict, coordenates: tuple):
    return places.get(coordenates, 'A coordenada não foi encontrada')


print(find_place(coordenadas, coordenada_sao_paulo))
print(find_place(coordenadas, (0, 0)))
