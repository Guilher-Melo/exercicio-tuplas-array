# Parte 1: Tuplas
# 1.1 Crie uma tupla para armazenar os códigos de cor RGB
#  (Vermelho, Verde, Azul),
#  usando os valores 255 para vermelho, 102 para verde e 0 para azul.

RGB = (255, 102, 0)

# 1.2 Crie uma tupla para as coordenadas geográficas,
# usando -8.0578 para latitude e -34.8829 para longitude.

coordenadas_geograficas = (-8.0578, -34.8829)

# 1.3 Crie uma tupla para armazenar as informações básicas
#  e imutáveis de um usuário, contendo o ID 101, o username 'ana_silva'
#  e a data de criação '2023-01-15'.

user_informations = (101, 'ana_silva', '2023-01-15')

# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e
#  imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).

print(RGB[1])

# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829),
#  desempacote-a em duas variáveis separadas chamadas latitude e longitude.

latitude = coordenadas_geograficas[0]
longitude = coordenadas_geograficas[1]

# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira',
#  'carlos.p@email.com'), que representa (id, nome, email),
#  desempacote-a em variáveis
#  e use a variável do nome para imprimir uma saudação.

usuario = (205, 'Carlos Pereira', 'carlos.p@email.com')
id = usuario[0]
nome = usuario[1]
email = usuario[2]

print(f'Olá, {nome}!')

# 1.7 Dada a tupla de papéis de administrador ('moderador',
#  'editor', 'sysadmin')
# , itere sobre ela e imprima cada papel.

papeis_adm = ('moderador', 'editor', 'sysadmin')

for papel in papeis_adm:
    print(papel)

# 1.8 Dada a tupla dados dos usuários acima,
#  itere sobre elas e imprima cada dado.

for user in usuario:
    print(user)

# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima
#  cada parte da cor, R, G e B.

for cor in RGB:
    print(cor)

# 1.10 Escreva uma função que verifique se um papel de usuário existe
#  em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin').
#  Teste a função com os papéis 'editor' e 'usuario_comum'.


def verify_user(role):
    roles = ('moderador', 'editor', 'sysadmin')

    if role in roles:
        print('Papel existe!')
    else:
        print('Usuário inválido!')


verify_user('editor')
verify_user('usuario_comum')

# 1.11 Dada a tupla de atribuições das pessoas de um equipe
#  ('editor', 'leitor', 'editor', 'comentarista',
#  'editor'), escreva uma função que conta o número de
#  vezes em que um papel aparece, teste a função com os papíes
# 'editor', 'comentarista' e 'tradutor'


def count_roles(role):
    roles = ('editor', 'leitor', 'editor', 'comentarista', 'editor')

    count = 0

    for new_role in roles:
        if new_role == role:
            count += 1

    return f'O papel {role} aparece {count} vez(es) na tupla'


print(count_roles('editor'))
print(count_roles('comentarista'))
print(count_roles('tradutor'))
