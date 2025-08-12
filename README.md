# Análise de Vendas e Performance (Power BI)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Numpy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-006F86?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-2391DF?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)](https://powerbi.microsoft.com/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-DDDDDD?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/python-dotenv/)
[![Status do Projeto](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](https://github.com/ravizeraig/DataProductsHelper)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Este projeto apresenta um dashboard interativo desenvolvido no Power BI para analisar o desempenho de vendas de uma empresa, com foco na evolução da receita, performance de produtos, desempenho de vendedores e distribuição regional das vendas.

## Funcionalidades e Insights Principais

O dashboard permite uma análise detalhada e interativa dos dados de vendas, incluindo:

* **Tendência de Vendas (Receita):** Acompanhamento da evolução mensal e anual da receita total, permitindo identificar padrões sazonais e crescimento ao longo do tempo.
* **Desempenho por Produto:** Visualização da receita gerada por cada produto, facilitando a identificação dos itens mais e menos vendidos.
* **Performance de Vendedores:** Análise da receita gerada por vendedor, incluindo ranking de vendas e tendência de desempenho individual ao longo dos meses.
* **Análise Regional:** Compreensão da distribuição das vendas por regiões geográficas (Norte, Nordeste, Sudeste, etc.), revelando as áreas de maior e menor contribuição para a receita.
* **Filtros Interativos:** Capacidade de filtrar todos os visuais por ano e mês, proporcionando flexibilidade na exploração dos dados.

## Estrutura do Projeto

A estrutura de diretórios do projeto está organizada da seguinte forma:

DataProductsHelper/
├── PowerBI/
│   └── dashboard_vendas.pbix        # Arquivo principal do dashboard Power BI
├── data/
│   ├── input/                     # Contém os arquivos CSV de dados brutos de origem
│   └── output/                    # Contém os arquivos CSV resultantes do processo de ETL (dados limpos e transformados)
├── notebooks/                     # Notebooks Jupyter para análise exploratória de dados (EDA) e prototipagem.
│   └── ... (diversos arquivos .ipynb que detalham análises e experimentos)
├── src/                           # Código-fonte Python principal do projeto
│   ├── analytics/                 # Módulos para lógica de análise de dados e geração de relatórios
│   │   ├── data_transformers.py   # Funções para transformações e agregações de dados específicas para análise
│   │   ├── report_generators.py   # Funções para gerar relatórios ou resumos de dados
│   │   └── sales_pricing_reporter.py # Módulo para relatórios focados em vendas e precificação
│   ├── config/                    # Módulos para configurações do projeto e variáveis de ambiente
│   │   └── settings.py            # Carrega e gerencia configurações e variáveis de ambiente
│   ├── data_managers/             # Módulos para gerenciamento de dados (geração e população)
│   │   ├── data_generator.py      # Script para gerar dados sintéticos (se aplicável)
│   │   └── data_populator.py      # Lógica para popular o banco de dados com dados iniciais
│   ├── database/                  # Módulos para interação com o banco de dados PostgreSQL
│   │   ├── db_builder.py          # Script para construir (criar tabelas) o esquema do banco de dados
│   │   ├── db_connector.py        # Gerencia a conexão com o banco de dados
│   │   ├── db_queries.py          # Contém as queries SQL para extração e manipulação de dados no DB
│   │   └── schema.sql             # Arquivo SQL com a definição do esquema do banco de dados (CREATE TABLE, etc.)
│   └── init.py                # Inicializa o pacote 'src'
├── .env                           # Arquivo para variáveis de ambiente (credenciais, tokens, etc. - IGNORADO pelo Git)
├── main.py                        # Ponto de entrada principal do projeto (orquestração do ETL/análise)
├── requirements.txt               # Lista de todas as bibliotecas Python necessárias para o projeto
├── .gitignore                     # Define arquivos e pastas a serem ignorados pelo controle de versão Git
└── LICENSE.md                     # Arquivo contendo a licença do projeto (ex: MIT License)

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter instalado:

* **Python 3.x**
* **PostgreSQL**: Um servidor de banco de dados PostgreSQL.
* **Power BI Desktop**: Para visualizar e interagir com o dashboard.

### Configuração do Ambiente

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/ravizeraig/DataProductsHelper.git](https://github.com/ravizeraig/DataProductsHelper.git)
    cd DataProductsHelper
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurações do Banco de Dados (.env):**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Copie o conteúdo de `.env.example` para `.env` e preencha com suas credenciais reais do PostgreSQL.
        ```ini
        # Exemplo de conteúdo para .env
        DB_HOST=your_db_host
        DB_NAME=your_db_name
        DB_USER=your_db_user
        DB_PASSWORD=your_db_password
        DB_PORT=5432
        ```

### Execução da Pipeline de Dados (ETL)

1.  **Execute o `main.py`:**
    * Este script é o ponto de entrada principal do projeto. Ele se conectará ao seu banco de dados PostgreSQL, verificará a existência do esquema, o criará (se necessário) e o populará com os dados iniciais. Além disso, ele deve orquestrar a limpeza e transformação dos dados, gerando os arquivos `.csv` limpos na pasta `data/output/`.

    ```bash
    python main.py
    ```
    * *Certifique-se de que o seu servidor PostgreSQL esteja em execução antes de rodar este comando.*

### Visualização no Power BI

1.  **Abra o Dashboard:**
    * Navegue até a pasta `PowerBI/`.
    * Abra o arquivo `dashboard_vendas.pbix` com o Power BI Desktop.
    * O dashboard está configurado para se conectar aos arquivos CSV limpos localizados em `data/output/`. Se houver qualquer problema de conexão de dados no Power BI, você pode precisar atualizar as origens de dados dentro do Power BI Desktop.

## 📊 Dados do Projeto

Para este projeto, foi criada uma base de dados PostgreSQL do zero, que foi populada integralmente com **dados simulados**. Estes dados foram gerados com o propósito de demonstrar a robustez da pipeline de ETL e a capacidade de análise e visualização.

## Tecnologias Utilizadas

As principais ferramentas e linguagens utilizadas no desenvolvimento deste projeto incluem:

* **Python 3.x**: Linguagem de programação principal para ETL, análise e orquestração.
* **Pandas**: Biblioteca para manipulação e análise de dados.
* **Psycopg2-binary**: Adaptador PostgreSQL para Python.
* **Python-dotenv**: Para gerenciamento seguro de variáveis de ambiente.
* **PostgreSQL:** Banco de dados relacional utilizado para armazenar os dados processados.
    * A estrutura do banco de dados foi criada do zero e populada com **dados simulados**, gerados exclusivamente para fins de demonstração da pipeline e da funcionalidade do projeto.

* **Jupyter Notebook**: Para análise exploratória de dados (EDA) e prototipagem.
* **Matplotlib, Seaborn, Plotly**: Bibliotecas para visualização de dados.
* **Power BI Desktop**: Ferramenta de Business Intelligence para criação do dashboard interativo.
* **Git**: Sistema de controle de versão.
* **GitHub**: Plataforma para hospedagem de código-fonte.

## Autor

* **Igor de Paula**
    * [LinkedIn](https://www.linkedin.com/in/depaulaiigor/)
    * [GitHub](https://github.com/ravizeraig)