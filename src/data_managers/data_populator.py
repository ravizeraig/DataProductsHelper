# src/data_managers/data_populator.py
import pandas as pd
from src.database.db_connector import get_db_connection, close_db_connection
import os

# Define o caminho para a pasta de entrada de dados
DATA_INPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'input')


def populate_products(file_path):
    """Carrega dados de produtos de um CSV e os insere na tabela Products."""
    df = pd.read_csv(file_path)
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            for index, row in df.iterrows():
                # Verifica se o produto já existe para evitar duplicatas em testes repetidos
                cursor.execute("SELECT id FROM Products WHERE nome_produto = %s;", (row['nome_produto'],))
                existing_product = cursor.fetchone()

                if existing_product:
                    print(f"Produto '{row['nome_produto']}' já existe. Ignorando inserção.")
                else:
                    insert_query = """
                    INSERT INTO Products (nome_produto, custo_producao_brl, margem_desejada_percentual, status, data_cadastro)
                    VALUES (%s, %s, %s, %s, %s);
                    """
                    cursor.execute(insert_query, (
                        row['nome_produto'],
                        row['custo_producao_brl'],
                        row['margem_desejada_percentual'],
                        row['status'],
                        row['data_cadastro']
                    ))
                    print(f"Produto '{row['nome_produto']}' inserido.")
            conn.commit()
            print(f"Dados de produtos de '{os.path.basename(file_path)}' carregados com sucesso.")
        except Exception as e:
            conn.rollback()
            print(f"Erro ao carregar dados de produtos: {e}")
        finally:
            close_db_connection(conn)


def populate_salespeople(file_path):
    """Carrega dados de vendedores de um CSV e os insere na tabela SalesPeople."""
    df = pd.read_csv(file_path)
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            for index, row in df.iterrows():
                insert_query = """
                INSERT INTO SalesPeople (id, nome_vendedor, email, telefone)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET
                    nome_vendedor = EXCLUDED.nome_vendedor,
                    email = EXCLUDED.email,
                    telefone = EXCLUDED.telefone;
                """
                cursor.execute(insert_query, (
                    int(row['id']), # Convert to int
                    row['nome_vendedor'],
                    row['email'],
                    row['telefone']
                ))
                print(f"Vendedor '{row['nome_vendedor']}' (ID: {int(row['id'])}) inserido/atualizado.")
            conn.commit()
            print(f"Dados de vendedores de '{os.path.basename(file_path)}' carregados com sucesso.")
        except Exception as e:
            conn.rollback()
            print(f"Erro ao carregar dados de vendedores: {e}")
        finally:
            close_db_connection(conn)


def populate_sales_goals(file_path):
    """Carrega dados de metas de vendas de um CSV e os insere na tabela SalesGoals."""
    print(f"\n--- Iniciando população de Metas de Vendas do arquivo: {file_path} ---")
    try:
        df = pd.read_csv(file_path)
        print(f"Lidas {len(df)} linhas do CSV de metas de vendas.")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado. Verifique o caminho e o nome do arquivo.")
        return
    except Exception as e:
        print(f"Erro ao ler o CSV de metas de vendas: {e}")
        return

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            for index, row in df.iterrows():
                # CONVERSÃO EXPLÍCITA DOS TIPOS AQUI PARA EVITAR ERROS DO PG
                goal_id = int(row['id'])
                goal_year = int(row['ano'])
                goal_month = int(row['mes'])
                goal_value = float(row['meta_vendas_brl'])

                print(f"Tentando inserir Meta: ID={goal_id}, Ano={goal_year}, Mês={goal_month}, Valor={goal_value}")
                insert_query = """
                INSERT INTO SalesGoals (id, ano, mes, meta_vendas_brl)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET
                    ano = EXCLUDED.ano,
                    mes = EXCLUDED.mes,
                    meta_vendas_brl = EXCLUDED.meta_vendas_brl;
                """
                cursor.execute(insert_query, (
                    goal_id,
                    goal_year,
                    goal_month,
                    goal_value
                ))
            conn.commit()
            print(f"Dados de metas de vendas de '{os.path.basename(file_path)}' carregados com sucesso.")
        except Exception as e:
            conn.rollback()
            print(f"Erro FATAL ao carregar dados de metas de vendas: {e}")
        finally:
            close_db_connection(conn)
    print("--- Fim da população de Metas de Vendas ---")


def populate_sales_and_projects(file_path):
    """
    Carrega dados de vendas e projetos de um CSV, insere ou atualiza,
    e associa IDs de produtos.
    """
    df = pd.read_csv(file_path)
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            for index, row in df.iterrows():
                # 1. Obter o ID do produto pelo nome
                cursor.execute("SELECT id FROM Products WHERE nome_produto = %s;", (row['produto_nome'],))
                product_id = cursor.fetchone()
                if not product_id:
                    print(
                        f"Erro: Produto '{row['produto_nome']}' não encontrado para o projeto '{row['projeto_nome']}'. Pulando.")
                    continue
                product_id = product_id[0]

                # 2. Inserir ou atualizar CommercialProjects
                cursor.execute("SELECT id FROM CommercialProjects WHERE nome_projeto = %s;", (row['projeto_nome'],))
                existing_project = cursor.fetchone()

                if existing_project:
                    project_id = existing_project[0]
                    update_project_query = """
                    UPDATE CommercialProjects SET
                        produto_id = %s, data_inicio = %s, data_fim = %s,
                        valor_proposto_brl = %s, status_negociacao = %s
                    WHERE id = %s;
                    """
                    cursor.execute(update_project_query, (
                        product_id,
                        pd.to_datetime(row['data_venda']).date(),
                        pd.to_datetime(row['data_venda']).date(),
                        row['valor_final_brl'],
                        row['status_negociacao_projeto'],
                        project_id
                    ))
                    print(f"Projeto '{row['projeto_nome']}' atualizado.")
                else:
                    insert_project_query = """
                    INSERT INTO CommercialProjects (nome_projeto, produto_id, data_inicio, data_fim, valor_proposto_brl, status_negociacao)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
                    """
                    cursor.execute(insert_project_query, (
                        row['projeto_nome'],
                        product_id,
                        pd.to_datetime(row['data_venda']).date(),
                        pd.to_datetime(row['data_venda']).date(),
                        row['valor_final_brl'],
                        row['status_negociacao_projeto']
                    ))
                    project_id = cursor.fetchone()[0]
                    print(f"Projeto '{row['projeto_nome']}' inserido com ID: {project_id}.")

                # 3. Inserir Sales (Vendas)
                insert_sale_query = """
                INSERT INTO Sales (projeto_id, data_venda, valor_final_brl, quantidade_vendida, vendedor_id, regiao, cota_meta_vendas_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(insert_sale_query, (
                    project_id,
                    row['data_venda'],
                    row['valor_final_brl'],
                    row['quantidade_vendida'],
                    int(row['vendedor_id']), # Garantir que vendedor_id é int
                    row['regiao'],
                    1  # Cota de vendas fixa para simplificar, pode ser ajustado
                ))
                print(f"Venda para projeto '{row['projeto_nome']}' registrada.")

            conn.commit()
            print(f"Dados de vendas e projetos de '{os.path.basename(file_path)}' carregados com sucesso.")
        except Exception as e:
            conn.rollback()
            print(f"Erro ao carregar dados de vendas e projetos: {e}")
        finally:
            close_db_connection(conn)


# Função principal para executar o carregamento
if __name__ == "__main__":
    print("Iniciando carregamento de dados iniciais...")

    products_file = os.path.join(DATA_INPUT_PATH, 'initial_products.csv')
    populate_products(products_file)

    salespeople_file = os.path.join(DATA_INPUT_PATH, 'initial_salespeople.csv')
    populate_salespeople(salespeople_file)

    sales_goals_file = os.path.join(DATA_INPUT_PATH, 'initial_salesgoals.csv')
    populate_sales_goals(sales_goals_file)

    sales_file = os.path.join(DATA_INPUT_PATH, 'simulated_sales.csv')
    populate_sales_and_projects(sales_file)

    print("\nProcesso de carregamento de dados concluído.")