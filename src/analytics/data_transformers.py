# src/analytics/data_transformers.py

import pandas as pd
import numpy as np


def transform_sales_summary_data(df_raw_sales):
    """
    Transforma os dados brutos de vendas para o formato do relatório de sumário.
    """
    df_sales_summary = df_raw_sales.groupby(['nome_produto', 'vendedor_id']).agg(
        total_vendas=('sale_id', 'count'),
        receita_total_brl=('valor_final_brl', 'sum'),
        quantidade_total_vendida=('quantidade_vendida', 'sum')
    ).reset_index()

    return df_sales_summary.sort_values(by='receita_total_brl', ascending=False)


def transform_pricing_analysis_data(df_raw_pricing):
    """
    Adiciona colunas calculadas para a análise de alinhamento de precificação.
    """
    df_pricing_data = df_raw_pricing.copy()

    # Calcular Preço Sugerido (com base no custo e margem desejada)
    df_pricing_data['preco_sugerido_brl'] = df_pricing_data['custo_producao_brl'] / (
                1 - df_pricing_data['margem_desejada_percentual'])

    # Calcular a Margem Real do Projeto (em relação ao custo, para comparar com a desejada)
    df_pricing_data['margem_real_projeto_percentual'] = np.where(
        df_pricing_data['custo_producao_brl'] > 0,
        (df_pricing_data['valor_final_projeto_brl'] - df_pricing_data['custo_producao_brl']) / df_pricing_data[
            'custo_producao_brl'],
        np.nan  # Se custo for 0, margem é indefinida
    )

    # Diferença percentual do valor final para o preço sugerido
    df_pricing_data['diferenca_percentual_sugerido'] = np.where(
        df_pricing_data['preco_sugerido_brl'] > 0,
        ((df_pricing_data['valor_final_projeto_brl'] - df_pricing_data['preco_sugerido_brl']) / df_pricing_data[
            'preco_sugerido_brl']),
        np.nan
    )

    return df_pricing_data