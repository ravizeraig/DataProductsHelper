# src/database/db_queries.py

import pandas as pd

def get_sales_summary_raw_data(conn):
    """
    Retorna os dados brutos necessários para o relatório de sumário de vendas.
    """
    query = """
    SELECT
        p.nome_produto,
        s.vendedor_id,
        s.id AS sale_id, -- Usado para COUNT na análise posterior
        s.valor_final_brl,
        s.quantidade_vendida,
        cp.status_negociacao
    FROM
        Sales s
    JOIN
        CommercialProjects cp ON s.projeto_id = cp.id
    JOIN
        Products p ON cp.produto_id = p.id
    WHERE
        cp.status_negociacao = 'Fechado';
    """
    return pd.read_sql(query, conn)

def get_pricing_analysis_raw_data(conn):
    """
    Retorna os dados brutos necessários para a análise de alinhamento de precificação.
    """
    query = """
    SELECT
        p.nome_produto,
        p.custo_producao_brl,
        p.margem_desejada_percentual,
        cp.valor_proposto_brl AS valor_final_projeto_brl,
        s.quantidade_vendida
    FROM
        Products p
    JOIN
        CommercialProjects cp ON p.id = cp.produto_id
    JOIN
        Sales s ON cp.id = s.projeto_id
    WHERE
        cp.status_negociacao = 'Fechado';
    """
    return pd.read_sql(query, conn)