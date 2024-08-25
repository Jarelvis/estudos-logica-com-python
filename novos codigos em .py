
# O algoritmo a seguir compara os preços dos itens da cesta básica em diferentes lojas e mostra o menor preço de cada item.
# Lista de itens da cesta básica
itens_cesta_basica = [
    "Arroz", "Feijão", "Açúcar", "Café", "Óleo", "Leite", "Farinha", "Macarrão"
]

# Dicionário para armazenar os preços dos itens em diferentes lojas
precos_lojas = {
    "Loja A": {},
    "Loja B": {},
    "Loja C": {}
}

# Função para adicionar preços de itens para uma loja específica
def adicionar_precos(loja, precos):
    if loja in precos_lojas:
        precos_lojas[loja] = precos
    else:
        print(f"Loja {loja} não encontrada.")

# Função para comparar os preços dos itens entre as lojas
def comparar_precos():
    for item in itens_cesta_basica:
        print(f"\nItem: {item}")
        menor_preco = float('inf')
        loja_menor_preco = ""
        for loja, precos in precos_lojas.items():
            if item in precos:
                preco = precos[item]
                print(f"{loja}: R${preco:.2f}")
                if preco < menor_preco:
                    menor_preco = preco
                    loja_menor_preco = loja
        print(f"Menor preço: {loja_menor_preco} com R${menor_preco:.2f}")

# Adicionando preços para as lojas
adicionar_precos("Loja A", {
    "Arroz": 20.50, "Feijão": 7.80, "Açúcar": 3.50, "Café": 8.90, "Óleo": 6.70, "Leite": 4.50, "Farinha": 2.80, "Macarrão": 3.20
})
adicionar_precos("Loja B", {
    "Arroz": 21.00, "Feijão": 7.50, "Açúcar": 3.60, "Café": 8.70, "Óleo": 6.90, "Leite": 4.40, "Farinha": 2.90, "Macarrão": 3.10
})
adicionar_precos("Loja C", {
    "Arroz": 19.90, "Feijão": 7.90, "Açúcar": 3.40, "Café": 9.00, "Óleo": 6.80, "Leite": 4.60, "Farinha": 2.85, "Macarrão": 3.25
})

# Comparar os preços dos itens entre as lojas
comparar_precos()