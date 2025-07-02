import numpy as np

# Parte 3: Vetores (Listas e NumPy)
# 3.1 Crie uma lista de hashtags (#) para redes sociais
#  chamada tags_post com os valores ['#tecnologia', '#python', '#programacao'].
#  Em seguida, adicione a tag '#dados' ao final da lista.

tags_post = ['#tecnologia', '#python', '#programacao']
tags_post.append('#dados')


# 3.2 Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados']
# , remova o elemento '#programacao'.

tags_post.remove('#programacao')

# 3.3 Dada a lista de tags ['#tecnologia', '#python', '#dados'],
#  verifique se a string '#importante' existe na lista.

if "#importante" in tags_post:
    print('Existe!')
else:
    print('Não existe!')

# 3.4 Importe a biblioteca numpy com o alias np. Crie um array NumPy
#  a partir da lista de itens vendidos da semana, em que os itens
#  são tuplas representando (produto, quantidade):
#  [('camiseta', 10), ('calça', 5), ('sapato', 2)].

produtos = np.array([('camiseta', 10), ('calça', 5), ('sapato', 2)])

# 3.5 Crie um array NumPy para armazenar as seguintes pontuações de um aluno:
#  [0.85, 0.92, 0.78, 0.95, 0.88].

pontos_aluno = np.array([0.85, 0.92, 0.78, 0.95, 0.88])

# 3.6 Crie um array NumPy para armazenar as temperaturas em Celsius:
#  [45.5, 46.0, 45.8, 47.1, 46.5].

temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])

# 3.7 Dado o array NumPy com tuplas de itens e preços
#  precos = np.array([(Sapato, 100.0), (Calça, 250.0), (Camiseta, 80.0),
#  (Tênis, 150.0)]),
#  crie um novo array aplicando um desconto de 10% a todos os elementos
#  (multiplicando por 0.9).

dt = np.dtype([('produto', 'U20'), ('preco', 'f8')])

precos = np.array([
    ('Sapato', 100.0),
    ('Calça', 250.0),
    ('Camiseta', 80.0),
    ('Tênis', 150.0)
], dtype=dt)

precos_com_desconto = np.array([
    (item['produto'], item['preco'] * 0.9)
    for item in precos
], dtype=dt)


# 3.8 Modifique o desconto aplicado acima para ser de 15%
#  e imprima todos os valores originais e com desconto no formato,
#  o <item> custava <preco_original>, agora custa <preco_com_desconto>.

precos_com_desconto_novo = np.array([
    (item['produto'], item['preco'] * 0.85)
    for item in precos
], dtype=dt)


for i in range(len(precos_com_desconto)):
    print(
        f'O {precos[i][0]} custava {precos[i][1]},\
 agora custa {precos_com_desconto[i][1]}'
    )

# 3.9 Dados o array de quantidades quantidades = np.array([1, 2, 3])
#  e o array de preços unitários precos_unitarios=np.array([15.0, 30.0, 22.5]),
#  calcule o valor total por item multiplicando os dois arrays.

quantidades = np.array([1, 2, 3])
precos_unitarios = np.array([15.0, 30.0, 22.5])

valor_total = quantidades * precos_unitarios

print(valor_total)

# 3.10 Dado o array de temperaturas em Celsius
#  temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5]),
#  converta todas as temperaturas para Fahrenheit
#  usando a fórmula F = C * 1.8 + 32.

temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])

temperaturas_fah = temperaturas_celsius * 1.8 + 32
