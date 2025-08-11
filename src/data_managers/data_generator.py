# src/data_managers/data_generator.py

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

# --- NOVAS LISTAS DE DADOS REAIS ---
# Lista de nomes de produtos mais realistas (você pode expandir essa lista!)
REAL_PRODUCT_NAMES = [
    "Smartphone Galaxy XYZ", "Smart TV QLED 55\"", "Geladeira Frost Free",
    "Máquina de Lavar 12kg", "Notebook Gamer G300", "Fone de Ouvido Bluetooth",
    "Echo Dot 4ª Geração", "Câmera Digital Profissional", "Aspirador de Pó Robô",
    "Forno Microondas Digital", "Air Fryer 4L", "Cafeteira Expresso",
    "Barbeador Elétrico", "Secador de Cabelo Profissional", "Cooktop 5 Bocas",
    "Lava-Louças Compacta", "Caixa de Som Portátil", "Monitor Gamer 27\"",
    "Impressora Multifuncional", "Roteador Wi-Fi 6", "Pneu Aro 16",
    "Bicicleta Ergométrica", "Kit Ferramentas Completo", "Panela de Pressão Elétrica",
    "Liquidificador Turbo", "Batedeira Planetária", "Sanduicheira Elétrica",
    "Ventilador de Torre", "Ar Condicionado Split 9000 BTUs", "Projetor Portátil",
    "Faqueiro Inox 24 Peças", "Jogo de Panelas Antiaderente", "Assadeira de Vidro",
    "Mesa de Centro Moderna", "Cadeira Gamer Confort", "Sofá 3 Lugares Reclinável",
    "Guarda-Roupa Casal", "Cama Box Queen Size", "Travesseiro de Espuma Viscoelástica",
    "Cortina Blackout", "Tapete Geométrico", "Abajur de Chão Decorativo",
    "Kit Lâmpadas LED Inteligentes", "Fechadura Digital Biométrica",
    "Aspirador de Água e Pó", "Pistola de Pintura Elétrica", "Furadeira de Impacto",
    "Serra Elétrica Circular", "Lixadeira Orbital", "Trena a Laser",
    "Kit Chaves Combinadas", "Serra Tico-Tico", "Bateria Portátil Power Bank",
    "Webcam Full HD", "Microfone Condensador USB", "Controle Xbox Wireless",
    "Teclado Mecânico RGB", "Mouse Gamer Óptico", "Headset Gamer Surround",
    "Smartwatch Esportivo", "Balança Digital Bioimpedância", "Massageador Portátil",
    "Umidificador de Ar", "Purificador de Água", "Filtro de Barro Tradicional",
    "Chaleira Elétrica", "Sanduicheira Grill", "Grill Elétrico Multiúso",
    "Pipoca Elétrica", "Máquina de Costura Doméstica", "Ferro de Passar a Vapor",
    "Tábua de Passar Roupa", "Armário Multiuso", "Estante para Livros",
    "Cômoda 4 Gavetas", "Mesa de Jantar 4 Cadeiras", "Cozinha Compacta",
    "Cadeira de Escritório Ergonômica", "Banco de Jardim de Madeira",
    "Mangueira de Jardim Flexível", "Vaso Sanitário com Caixa Acoplada",
    "Chuveiro Elétrico Digital", "Torneira Gourmet Flexível", "Kit de Jardinagem",
    "Esmerilhadeira Angular", "Roçadeira a Gasolina", "Lavadora de Alta Pressão",
    "Bomba Submersa", "Motor de Popa", "Barraca de Camping 4 Pessoas",
    "Saco de Dormir Ultraleve", "Mochila de Ataque 40L", "Cantil Térmico",
    "Lanterna Tática LED", "Kit Sobrevivência Aventura", "Corda de Escalada",
    "Bússola Profissional", "Binóculos de Visão Noturna", "Drone com Câmera 4K",
    "Skate Elétrico Off-Road", "Patins Inline Ajustável", "Capacete de Moto Esportivo",
    "Luvas de Proteção Moto", "Jaqueta Motoqueiro Couro", "Calça Jeans Motoqueiro",
    "Botas de Moto Impermeáveis", "GPS Automotivo", "Central Multimídia Android",
    "Câmera de Ré para Carro", "Sensor de Estacionamento", "Alarme Automotivo",
    "Capa de Carro Protetora", "Kit Limpeza Automotiva", "Polidor de Carro Elétrico"
]

# Lista de regiões brasileiras
BRAZILIAN_REGIONS = [
    "Sudeste", "Sul", "Centro-Oeste", "Nordeste", "Norte"
]
# --- FIM DAS NOVAS LISTAS ---

# Define o caminho para a pasta de saída de dados
DATA_OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'input')


def generate_products_data(num_products=100): # Mudei o default para 100 para condizer com o número de nomes
    """
    Gera dados sintéticos para a tabela Products.
    """
    # --- MODIFICAÇÃO AQUI: USANDO NOMES REAIS ---
    # Garante que não haverá mais produtos do que nomes reais, ou usa um fallback
    if num_products > len(REAL_PRODUCT_NAMES):
        print(f"Atenção: num_products ({num_products}) é maior que o número de nomes reais ({len(REAL_PRODUCT_NAMES)}). Nomes serão repetidos ou genéricos extras.")
        # Se quiser mais produtos que nomes reais, pode usar random.choice ou gerar variantes
        product_names = [random.choice(REAL_PRODUCT_NAMES) for _ in range(num_products)]
    else:
        product_names = random.sample(REAL_PRODUCT_NAMES, num_products) # Pega amostra única

    # Se você tinha 'product_names = [f"Produto Genérico {i:04d}" for i in range(num_products)]'
    # Esta parte é substituída pela lógica acima.
    # --- FIM DA MODIFICAÇÃO DE NOMES DE PRODUTOS ---

    product_costs = np.round(np.random.uniform(50.00, 5000.00, num_products), 2)
    desired_margins = np.round(np.random.uniform(0.15, 0.60, num_products), 2)  # 15% a 60%
    statuses = np.random.choice(['Ativo', 'Inativo'], num_products, p=[0.9, 0.1])  # 90% Ativo

    # Datas de cadastro variando nos últimos 2 anos
    start_date = datetime.now() - timedelta(days=730)  # 2 anos atrás
    end_date = datetime.now()

    data_cadastro = [
        start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
        for _ in range(num_products)
    ]

    df_products = pd.DataFrame({
        'nome_produto': product_names,
        'custo_producao_brl': product_costs,
        'margem_desejada_percentual': desired_margins,
        'status': statuses,
        'data_cadastro': data_cadastro
    })

    output_file = os.path.join(DATA_OUTPUT_PATH, 'initial_products.csv')
    df_products.to_csv(output_file, index=False)
    print(f"Gerados {num_products} produtos em '{output_file}'")
    return df_products


def generate_sales_data(df_products, num_sales=50000):
    """
    Gera dados sintéticos para as tabelas Sales e CommercialProjects,
    baseando-se nos produtos gerados.
    """
    if df_products.empty:
        print("Nenhum produto gerado. Não é possível gerar dados de vendas.")
        return pd.DataFrame() # Retorna um DataFrame vazio para evitar erros

    sales_data = []
    project_statuses = ['Fechado', 'Em Proposta', 'Perdido']
    vendedor_ids = list(range(101, 111))  # 10 vendedores simulados

    # Gerar datas de venda nos últimos 18 meses
    start_date = datetime.now() - timedelta(days=540)  # 18 meses atrás
    end_date = datetime.now()

    # Pre-calcular product_ids para otimização se df_products for muito grande
    product_ids_list = df_products['id'].tolist() if 'id' in df_products.columns else list(range(len(df_products)))


    for i in range(num_sales):
        # Escolhe um produto aleatoriamente
        # Certifique-se de que o 'id' do produto é usado aqui se ele estiver disponível e for o que você quer
        # Se você está gerando o CSV e depois populando o DB, o 'nome_produto' pode ser suficiente aqui,
        # e o 'produto_id' viria do DF de produtos carregado no data_populator.
        # Por enquanto, vamos manter a lógica de usar o nome do produto para o 'projeto_nome'.
        product = df_products.sample(1).iloc[0]
        # Aqui, o product['id'] seria o ID gerado pelo DB, mas como estamos gerando CSV primeiro,
        # vamos usar o nome_produto para o projeto_nome e ligar via nome no populator se necessário.
        # Ou, idealmente, você teria gerado IDs para os produtos aqui também e usaria esses IDs.
        # Por enquanto, se o 'id' não for gerado aqui, o link é via 'nome_produto'
        # ou se o data_populator é inteligente para procurar o ID do produto pelo nome.
        # Para Sales, precisamos do projeto_id, não do produto_id diretamente.

        # Gera uma data de venda aleatória
        sale_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

        # Quantidade vendida (varia mais para produtos de menor custo)
        quantity = max(1, int(np.random.normal(50 / (product['custo_producao_brl'] / 1000 + 0.1),
                                               10)))

        # Valor final com base no custo, margem e um pouco de variância
        base_price_per_unit = product['custo_producao_brl'] / (1 - product['margem_desejada_percentual'])
        price_adjustment = np.random.uniform(0.9, 1.1)
        final_value_per_unit = np.round(base_price_per_unit * price_adjustment, 2)
        valor_final_brl = np.round(final_value_per_unit * quantity, 2)

        # Define o status do projeto
        status_proj = np.random.choice(project_statuses, p=[0.7, 0.2, 0.1])

        # Se for "Perdido" ou "Em Proposta", o valor final pode ser 0
        if status_proj == 'Perdido':
            valor_final_brl = 0.00
        elif status_proj == 'Em Proposta':
            # Manter o valor_final_brl como o valor proposto para simular negociação em andamento
            pass

        vendedor = random.choice(vendedor_ids)
        regiao = random.choice(BRAZILIAN_REGIONS) # <-- NOVO: GERE A REGIÃO PARA CADA VENDA

        sales_data.append({
            'projeto_nome': f"Venda {product['nome_produto']} - {i + 1}", # Usando o nome real do produto aqui
            'produto_nome': product['nome_produto'], # Mantendo para referência no CSV
            'data_venda': sale_date.strftime('%Y-%m-%d %H:%M:%S'),
            'valor_final_brl': valor_final_brl,
            'quantidade_vendida': quantity,
            'vendedor_id': vendedor,
            'regiao': regiao, # <-- NOVO: INCLUA A REGIÃO NO DICIONÁRIO
            'status_negociacao_projeto': status_proj
        })

    df_sales = pd.DataFrame(sales_data)
    output_file = os.path.join(DATA_OUTPUT_PATH, 'simulated_sales.csv')
    df_sales.to_csv(output_file, index=False)
    print(f"Geradas {num_sales} vendas em '{output_file}'")
    return df_sales


if __name__ == "__main__":
    print("Iniciando a geração de dados sintéticos...")

    # Geração de 100 produtos (para corresponder à lista de nomes reais)
    # Se quiser mais de 100 produtos únicos, você precisará expandir a lista REAL_PRODUCT_NAMES
    # ou ajustar a lógica em generate_products_data para gerar mais nomes únicos/variações.
    generated_products_df = generate_products_data(num_products=100) # Ajuste aqui se precisar de mais nomes

    # Verifique o número de produtos gerados vs. nomes reais disponíveis
    if len(generated_products_df) < len(REAL_PRODUCT_NAMES):
        print(f"AVISO: Gerados apenas {len(generated_products_df)} produtos, mas há {len(REAL_PRODUCT_NAMES)} nomes reais disponíveis. Considere aumentar num_products.")

    generate_sales_data(generated_products_df, num_sales=50000)

    print("\nGeração de dados concluída. Próximo passo: Rodar o data_populator.py novamente.")