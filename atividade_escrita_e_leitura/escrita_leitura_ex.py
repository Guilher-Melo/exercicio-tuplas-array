# flake8:noqa

# ==================================================
# BLOCO 1: ARQUIVOS TXT (15 exercícios)
# ==================================================

# --- Introdução ---
# Para arquivos TXT, usamos funções nativas do Python: open(), read(), write(), close()

import json
import re
# Exercício 1.1 (Resolvido)
# Crie um arquivo 'diario.txt' e registre uma entrada de diário sobre seu dia.
import zipfile

with open('src/diario.txt', 'w') as file:
    file.write("Hoje aprendi a manipular arquivos em Python!\n")

# Exercício 1.2
# Crie um arquivo 'tarefas.txt' e adicione 3 tarefas diárias.
with open('src/tarefas.txt', 'w', encoding='UTF-8') as file:
    file.write('Ir para a academia\n')
    file.write('Fazer mini projeto 6\n')
    file.write('Fazer exercício de python\n')

# Exercício 1.3
# Crie um arquivo 'metas.txt' registrando 2 metas pessoais para o ano.
with open('src/metas.txt', 'w') as file:
    file.write('Aprender a dirigir\n')
    file.write('Me exercitar mais birl')

# Exercício 1.4 (Resolvido)
# Leia o conteúdo do arquivo 'diario.txt' e imprima na tela.
with open('src/diario.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

# Exercício 1.5
# Leia o arquivo 'tarefas.txt' e mostre cada tarefa com um número de prefixo.
with open('src/tarefas.txt', 'r', encoding='utf-8') as file:
    n = 1
    for line in file:
        print(f'{n}- {line.strip()}')
        n += 1


# Exercício 1.6
# Leia 'metas.txt' e formate a saída com um '-' no começo de cada linha.

with open('src/metas.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(f'- {line.strip()}')

# Exercício 1.7 (Resolvido)
# Adicione uma nova linha ao final do 'diario.txt' sem apagar o conteúdo existente.
with open('src/diario.txt', 'a') as file:
    file.write("Agora estou praticando escrita de arquivos!\n")

# Exercício 1.8
# Adicione uma nova tarefa ao 'tarefas.txt' sem apagar as existentes.

with open('src/tarefas.txt', 'a') as file:
    file.write('Arrumar a casa...')

# Exercício 1.9
# Registre o progresso de uma meta no 'metas.txt'.

with open('src/metas.txt', 'a') as file:
    file.write('\n\n Ontem dei uma volta de carro pelo meu bairro')

# Exercício 1.10 (Resolvido)
# Conte quantas linhas existem no arquivo 'diario.txt'.
with open('src/diario.txt', 'r') as file:
    linhas = file.readlines()
    print(f"Total de entradas no diário: {len(linhas)}")

# Exercício 1.11
# Conte quantas tarefas estão registradas em 'tarefas.txt'.

with open('src/tarefas.txt', 'r') as file:
    total_tasks = file.readlines()
    print(f'Tarefas resgistradas: {len(total_tasks)}')

# Exercício 1.12
# Verifique se a palavra "urgente" aparece em qualquer tarefa.

with open('src/tarefas.txt', 'r', encoding='utf-8') as file:
    tasks = file.readlines()
    urgente = False
    for task in tasks:
        if 'urgente' in task:
            urgente = True
            break

    if urgente:
        print('Existe uma tarefa com urgência!!')
    else:
        print('Não existe tarefa com urgência :)')

# Exercício 1.13 (Resolvido)
# Crie um backup do diário chamado 'diario_backup.txt'.
with open('src/diario.txt', 'r') as origem, open('src/diario_backup.txt', 'w') as destino:
    destino.write(origem.read())

# Exercício 1.14
# Crie um backup das tarefas com data no nome do arquivo.
from datetime import date

with open('src/tarefas.txt', 'r') as origem, open(f'src/tarefas_backup_{date.today()}.txt', 'w') as destino:
    destino.write(origem.read())

# Exercício 1.15
# Transforme todas as metas em maiúsculas em um novo arquivo 'metas_prioridade.txt'.

with open('src/metas.txt', 'r') as origem, open('src/metas_prioridades.txt', 'w') as destino:
    metas = origem.readlines()

    for meta in metas:
        destino.write(meta.upper())

# ==================================================
# BLOCO 2: ARQUIVOS CSV (15 exercícios)
# ==================================================

# --- Introdução ---
import csv

# Exercício 2.1 (Resolvido)
# Crie um arquivo 'contatos.csv' com cabeçalhos: nome,email,telefone
cabecalhos = ['nome', 'email', 'telefone']
contatos = [
    ['Ana Silva', 'ana@email.com', '(11) 91234-5678'],
    ['Carlos Oliveira', 'carlos@empresa.com', '(21) 99876-5432']
]

with open('src/contatos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalhos)
    writer.writerows(contatos)

# Exercício 2.2
# Crie um CSV 'produtos.csv' com campos: id,nome,preço,estoque
cabecalho = ['id', 'nome', 'preço', 'estoque']
produtos = [
    ['01', 'Caneta', 10.29, 260],
    ['02', 'Caderno', 120.29, 30],
    ['04', 'Calculadora', 16.30, 12],
    ['05', 'Caixa de lápis', 109.29, 20],
]

with open('src/produtos.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalho)
    writer.writerows(produtos)

# Exercício 2.3
# Crie um CSV 'eventos.csv' para registrar shows: artista,local,data,ingressos

cabecalho = ['artista', 'local', 'data', 'ingressos']
eventos = [
    ['Santanna O Cantador', 'Classic Hall', '30/10/2015', 800],
    ['Guns n Roses', 'Arena Pernambuco', '12/08/2025', 30000],
    ['Belo Cover', 'Bar do seu Zé', '10/03/2026', 120],
]

with open('src/eventos.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalho)
    writer.writerows(eventos)

# Exercício 2.4 (Resolvido)
# Leia 'contatos.csv' e mostre os dados em formato de tabela
with open('src/contatos.csv', newline='') as file:
    reader = csv.reader(file)
    for linha in reader:
        print(f"{linha[0]:<20} | {linha[1]:<20} | {linha[2]}")

# Exercício 2.5
# Leia 'produtos.csv' e calcule o valor total do estoque

with open('src/produtos.csv', 'r', encoding='utf-8') as file:
    coluna = 3
    linha_index = 1
    reader = csv.reader(file)
    total_estoque = 0
    for linha in reader:
        try:
            total_produto = float(linha[2]) * float(linha[3])
            total_estoque += total_produto
        except:
            pass

    print(f'total do estoque: R${total_estoque}')


# Exercício 2.6
# Leia 'eventos.csv' e mostre apenas eventos com ingressos disponíveis

with open('src/eventos.csv', 'r', encoding='utf-8') as file:
    eventos = csv.reader(file)

    for evento in eventos:
        try:
            ingressos = int(evento[3])

            if ingressos > 0:
                print(f'Ingressos disponíveis: {ingressos}')
        except:
            pass

# Exercício 2.7 (Resolvido)
# Adicione um novo contato ao 'contatos.csv'
novo_contato = ['Maria Santos', 'maria@tech.com', '(31) 94567-1234']
with open('src/contatos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(novo_contato)

# Exercício 2.8
# Adicione 3 novos produtos ao 'produtos.csv'

novo_produto = [10, 'Cueca', 79.90, 5]
with open('src/produtos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(novo_produto)

# Exercício 2.9
# Registre um novo show no 'eventos.csv'

novo_evento = ['Xuxa', 'Arena', '20/09/2026', 50]
with open('src/eventos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(novo_evento)

# Exercício 2.10 (Resolvido)
# Converta o CSV para dicionário e encontre contatos com domínio específico
with open('src/contatos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if 'empresa.com' in contato['email']:
            print(f"Contato corporativo: {contato['nome']}")

# Exercício 2.11
# Calcule a média de preços dos produtos usando dicionários

with open('src/produtos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    total_preco = 0
    qnt_produtos = 0
    for produto in reader:
        total_preco += float(produto['preço'])
        qnt_produtos += 1
    media = total_preco/qnt_produtos
    print(f'Média preços: {media}')

# Exercício 2.12
# Atualize a quantidade de ingressos para um evento específico

# Exercício 2.13 (Resolvido)
# Valide telefones no formato (XX) XXXXX-XXXX

with open('src/contatos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if not re.match(r'\(\d{2}\) \d{5}-\d{4}', contato['telefone']):
            print(f"Telefone inválido: {contato['nome']}")

# Exercício 2.14
# Valide se todos os IDs de produtos são únicos

valores = set()

with open('src/produtos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for produto in reader:
        valor = produto['id']
        if valor in valores:
            print(f"Duplicado encontrado: {valor}")
            break
        valores.add(valor)
    else:
        print("Todos os valores são únicos.")

# Exercício 2.15
# Crie um sistema de busca por artista no 'eventos.csv'

with open('src/eventos.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    artista = input('Digite o nome do artista: ')

    artista_encontrado = False

    for evento in reader:
        if artista in evento['artista']:
            print('Artista encontrado!')
            print(evento)
            artista_encontrado = True
    if not artista_encontrado:
        print('Não temos um evento com esse artista...')


# ==================================================
# ==================================================
# BLOCO 3: ARQUIVOS JSON (15 exercícios) - TEMA: JOGOS E REDES SOCIAIS
# ==================================================

# --- Introdução ---

# Exercício 3.1 (Resolvido)
# Salve os dados de um personagem de RPG em 'personagem.json': nome, nível, pontos de vida, habilidades e equipamentos
personagem = {
    "nome": "Arya Stark",
    "nivel": 15,
    "hp": 320,
    "habilidades": ["Agilidade", "Furtividade", "Disfarces"],
    "equipamentos": {
        "arma": "Agulha",
        "armadura": "Couro",
        "anel": "Nenhum"
    }
}

with open('src/personagem.json', 'w') as file:
    json.dump(personagem, file, indent=4)

# Exercício 3.2
# Crie um arquivo 'perfil_instagram.json' com dados de um influenciador: username, seguidores, seguindo, posts e biografia

influencer = {
    'username': 'brunorsouza',
    'seguidores': 30000,
    'seguindo': 30,
    'posts': [
        {
            'titulo': 'Na praia tche tche',
            'likes': 90000,
            'data': '20/01/2025'
        },
        {
            'titulo': 'Frio bom',
            'likes': 50000,
            'data': '20/07/2024'
        }
    ],
    'biografia': 'Cientista da computação em formação - UFRPE, sommelier de RU.'
}

with open('src/perfil_instagram.json', 'w', encoding='utf-8') as file:
    json.dump(influencer, file, indent=4)

# Exercício 3.3
# Armazene os dados de um monstro em 'monstro.json': nome, tipo, nível, pontos_ataque e recompensas

monstro = {
    "nome": "Ogro",
    "tipo": "Lutador",
    "nivel": 8,
    "pontos_ataque": 20,
    "recompensas": [
        {"nome": "Bau",
         "valor": 2},
        {"nome": "Armadura",
         "valor": 5},
    ]
}

with open('src/monstro.json', 'w', encoding='utf-8') as file:
    json.dump(monstro, file, indent=4)
# Exercício 3.4 (Resolvido)
# Leia 'personagem.json' e mostre as habilidades do personagem
with open('src/personagem.json') as file:
    dados = json.load(file)
    print("Habilidades:", ", ".join(dados['habilidades']))

# Exercício 3.5
# Leia 'perfil_instagram.json' e calcule a taxa de engajamento (média de likes por post)

with open('src/perfil_instagram.json') as file:
    perfil = json.load(file)

    total_likes = 0

    posts = perfil['posts']

    for post in posts:
        total_likes += post['likes']

    media_likes = total_likes/len(posts)

    print(f'A média de likes é: {media_likes}')


# Exercício 3.6
# Leia 'monstro.json' e mostre a recompensa mais valiosa

with open('src/monstro.json', 'r') as file:
    dados = json.load(file)
    maior_valor = max(dados['recompensas'], key=lambda d: d['valor'])

    print(f'O item de maior valor é: {maior_valor}')


# Exercício 3.7 (Resolvido)
# Atualize o nível do personagem para 16 e salve no arquivo
with open('src/personagem.json') as file:
    dados = json.load(file)

    dados['nível'] = 16

with open('src/personagem.json', 'w') as file:
    json.dump(dados, file, indent=4)

# Exercício 3.8
# Adicione um novo post ao perfil do Instagram com data e likes

novo_post = {
    "titulo": "Novo post incrível",
    "likes": "25000",
    "data": "07/07/2025"
}

with open('src/perfil_instagram.json', 'r') as file:
    perfil = json.load(file)

perfil['posts'].append(novo_post)

with open('src/perfil_instagram.json', 'w', encoding='utf-8') as file:
    json.dump(perfil, file, ensure_ascii=False, indent=4)

# Exercício 3.9
# Atualize os pontos de ataque do monstro após uma evolução

with open('src/monstro.json') as file:
    dados = json.load(file)

    dados['pontos_ataque'] = 25

with open('src/monstro.json', 'w') as file:
    json.dump(dados, file, indent=4)

# Exercício 3.10 (Resolvido)
# Valide se o personagem tem equipamento de arma
with open('src/personagem.json') as file:
    dados = json.load(file)
    if "arma" in dados['equipamentos'] and dados['equipamentos']['arma']:
        print("Personagem está armado!")
    else:
        print("Personagem desarmado!")

# Exercício 3.11
# Verifique se o perfil do Instagram tem mais de 10.000 seguidores

with open('src/perfil_instagram.json', 'r') as file:
    dados = json.load(file)

    if dados['seguidores'] > 10000:
        print('Tem mais de 10000 seguidores')
    else:
        print('Não tem mais de 10000 seguidores')

# Exercício 3.12
# Calcule o valor total das recompensas do monstro

with open('src/monstro.json', 'r') as file:
    dados = json.load(file)

    recompensas_totais = sum(m['valor'] for m in dados['recompensas'])

    print(f'Recompensas totais: {recompensas_totais}')


# Exercício 3.13 (Resolvido)
# Converta os dados do personagem para string JSON e salve em formato minificado
personagem_str = json.dumps(personagem, separators=(',', ':'))
with open('src/personagem_min.json', 'w') as file:
    file.write(personagem_str)

# Exercício 3.14
# Crie um backup do perfil do Instagram com a data atual no nome do arquivo

with open('src/perfil_instagram.json') as origem, open(f'src/perfil_instagram_{date.today()}.json', 'w') as destino:
    destino.write(origem.read())


# Exercício 3.15
# Combine dados de múltiplos personagens em um arquivo 'grupo.json'

personagem_2 = {
    "nome": "Jon Snow",
    "nivel": 12,
    "hp": 450,
    "habilidades": ["Sorte", "Liderança", "Resiliência"],
    "equipamentos": {
        "arma": "Espada",
        "armadura": "Metal",
        "anel": "Nenhum"
    }
}
personagem_3 = {
    "nome": "Hodor",
    "nivel": 17,
    "hp": 900,
    "habilidades": ["Força", "Resistência", "Grupo"],
    "equipamentos": {
        "arma": "Mãos",
        "armadura": "Nenhum",
        "anel": "Nenhum"
    }
}

grupo = [personagem, personagem_2, personagem_3]

with open('src/grupo.json', 'w', encoding='utf-8') as file:
    json.dump(grupo, file, ensure_ascii=False, indent=4)

# ==================================================
# BLOCO 4: EXERCÍCIOS MISTOS (5 exercícios)
# ==================================================

# Exercício 4.1 (Resolvido)
# Converta dados de personagens de JSON para CSV


def json_para_csv(origem, destino):
    with open(origem) as json_file:
        dados = json.load(json_file)

    with open(destino, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dados.keys())
        writer.writerow(dados.values())


# Teste:
json_para_csv('src/personagem.json', 'src/personagem.csv')

# Exercício 4.2
# Crie um sistema de inventário que salva itens coletados em TXT, CSV e JSON

inventario = [
    {"item": "Espada de Ferro", "quantidade": 1},
    {"item": "Poção de Vida", "quantidade": 3},
    {"item": "Escudo de Madeira", "quantidade": 1},
]

with open("src/inventario.txt", "w") as txt_file:
    for item in inventario:
        txt_file.write(f"{item['item']}: {item['quantidade']}\n")

with open("src/inventario.csv", "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["item", "quantidade"])
    writer.writeheader()
    writer.writerows(inventario)

with open("src/inventario.json", "w") as json_file:
    json.dump(inventario, json_file, indent=4)


# Exercício 4.3
# Desenvolva um feed de notícias de jogo que salva em JSON e exporta para TXT

feed = [
    {"titulo": "Chefe Derrotado",
        "descricao": "O jogador venceu o Dragão de Fogo!", "data": "2025-07-09"},
    {"titulo": "Item Raro Encontrado",
        "descricao": "Espada Lendária foi descoberta na masmorra.", "data": "2025-07-08"},
]

with open("src/feed.json", "w") as json_file:
    json.dump(feed, json_file, indent=4)


with open("src/feed.txt", "w") as txt_file:
    for noticia in feed:
        txt_file.write(
            f"{noticia['data']} - {noticia['titulo']}\n{noticia['descricao']}\n\n")

# Exercício 4.4
# Crie um analisador de perfil social que lê JSON e gera relatório em CSV

with open('src/perfil_instagram.json', 'r', encoding='utf-8') as f:
    perfis = json.load(f)

with open('src/relatorio.csv', 'w', newline='', encoding='utf-8') as csvfile:
    campos = ['username', 'seguidores', 'seguindo',
              'posts_total', 'media_likes', 'taxa_engajamento_%']
    writer = csv.DictWriter(csvfile, fieldnames=campos)

    writer.writeheader()

    username = perfis['username']
    seguidores = perfis['seguidores']
    seguindo = perfis['seguindo']
    posts = perfis['posts']
    total_posts = len(posts)

    likes_totais = sum(int(post['likes']) for post in posts)
    media_likes = likes_totais / total_posts if total_posts else 0

    taxa_engajamento = (media_likes / seguidores) * \
        100 if seguidores else 0

    writer.writerow({
        'username': username,
        'seguidores': seguidores,
        'seguindo': seguindo,
        'posts_total': total_posts,
        'media_likes': round(media_likes, 2),
        'taxa_engajamento_%': round(taxa_engajamento, 2)
    })

print("Relatório gerado: relatorio.csv")

# Exercício 4.5
# Implemente um sistema de save game que compacta dados em ZIP


save_game = {
    "jogador": "HeroiXP",
    "nivel": 12,
    "itens": ["Espada", "Escudo", "Poção"]
}

with open("src/save_game.json", "w") as f:
    json.dump(save_game, f, indent=4)

with zipfile.ZipFile("src/save_game.zip", "w") as zipf:
    zipf.write("src/save_game.json")
