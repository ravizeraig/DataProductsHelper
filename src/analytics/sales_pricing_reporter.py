# src/analytics/sales_pricing_reporter.py

from src.database.db_connector import get_db_connection, close_db_connection
from src.database.db_queries import get_sales_summary_raw_data, get_pricing_analysis_raw_data
from src.analytics.data_transformers import transform_sales_summary_data, transform_pricing_analysis_data
from src.analytics.report_generators import save_dataframe_to_csv, save_dataframe_to_excel

def generate_all_reports():
    """
    Orquestra a extração, transformação e geração de todos os relatórios.
    """
    conn = get_db_connection()
    if not conn:
        print("Não foi possível estabelecer conexão com o banco de dados.")
        return

    try:
        # --- Relatório de Sumário de Vendas ---
        print("Iniciando geração do Relatório de Sumário de Vendas...")
        raw_sales_df = get_sales_summary_raw_data(conn)
        if raw_sales_df.empty:
            print("Nenhum dado bruto de vendas encontrado para o sumário.")
        else:
            sales_summary_df = transform_sales_summary_data(raw_sales_df)
            save_dataframe_to_csv(sales_summary_df, 'sales_summary_report.csv')
            print("\nPrimeiras 5 linhas do Relatório de Sumário de Vendas:")
            print(sales_summary_df.head())

        print("\n---------------------------------------------------")

        # --- Análise de Alinhamento de Precificação ---
        print("Iniciando geração da Análise de Alinhamento de Precificação...")
        raw_pricing_df = get_pricing_analysis_raw_data(conn)
        print("\n--- DEBUG: raw_pricing_df head ---")
        print(raw_pricing_df.head())
        print(f"--- DEBUG: raw_pricing_df is empty: {raw_pricing_df.empty}")
        if raw_pricing_df.empty:
            print("Nenhum dado bruto de precificação encontrado para análise.")
        else:
            pricing_analysis_df = transform_pricing_analysis_data(raw_pricing_df)
            save_dataframe_to_excel(pricing_analysis_df, 'product_pricing_analysis.xlsx')
            print("\nPrimeiras 5 linhas da Análise de Alinhamento de Precificação:")
            print(pricing_analysis_df.head())

    except Exception as e:
        print(f"Ocorreu um erro durante a geração de relatórios: {e}")
    finally:
        close_db_connection(conn)
        print("\nProcesso de relatórios concluído.")

if __name__ == "__main__":
    generate_all_reports()