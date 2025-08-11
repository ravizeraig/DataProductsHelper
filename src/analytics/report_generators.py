# src/analytics/report_generators.py

import os

# Define o caminho para a pasta de saída dos relatórios
# Assume que este arquivo está em src/analytics
REPORT_OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'output')

def save_dataframe_to_csv(df, filename):
    """Salva um DataFrame em um arquivo CSV na pasta de saída."""
    output_file = os.path.join(REPORT_OUTPUT_PATH, filename)
    df.to_csv(output_file, index=False)
    print(f"Relatório gerado com sucesso em '{output_file}'")

def save_dataframe_to_excel(df, filename):
    """Salva um DataFrame em um arquivo Excel na pasta de saída."""
    output_file = os.path.join(REPORT_OUTPUT_PATH, filename)
    df.to_excel(output_file, index=False)
    print(f"Relatório gerado com sucesso em '{output_file}'")