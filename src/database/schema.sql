-- src/database/schema.sql

-- **COMANDOS DE DROP PARA RECRIAÇÃO LIMPA**
-- Drop tables if they exist to allow clean recreation
-- A ordem é importante devido às chaves estrangeiras (FOREIGN KEYS)
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS CommercialProjects CASCADE;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS SalesPeople CASCADE;
DROP TABLE IF EXISTS SalesGoals CASCADE;

-- **CRIAÇÃO DAS TABELAS**

-- Create Products Table
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    nome_produto VARCHAR(255) UNIQUE NOT NULL,
    custo_producao_brl DECIMAL(10, 2) NOT NULL,
    margem_desejada_percentual DECIMAL(5, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    data_cadastro DATE NOT NULL
);

-- Create SalesPeople Table
CREATE TABLE SalesPeople (
    id SERIAL PRIMARY KEY,
    nome_vendedor VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

-- Create SalesGoals Table
CREATE TABLE SalesGoals (
    id SERIAL PRIMARY KEY,
    ano INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    meta_vendas_brl DECIMAL(15, 2) NOT NULL,
    UNIQUE (ano, mes)
);

-- Create CommercialProjects Table
CREATE TABLE CommercialProjects (
    id SERIAL PRIMARY KEY,
    nome_projeto VARCHAR(255) UNIQUE NOT NULL,
    produto_id INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_proposto_brl DECIMAL(15, 2) NOT NULL,
    status_negociacao VARCHAR(50) NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES Products(id)
);

-- Create Sales Table
CREATE TABLE Sales (
    id SERIAL PRIMARY KEY,
    projeto_id INTEGER NOT NULL,
    data_venda DATE NOT NULL,
    valor_final_brl DECIMAL(15, 2) NOT NULL,
    quantidade_vendida INTEGER NOT NULL,
    vendedor_id INTEGER NOT NULL,
    regiao VARCHAR(100) NOT NULL, -- <<<< ESTA LINHA É CRUCIAL E DEVE ESTAR PRESENTE!
    cota_meta_vendas_id INTEGER NOT NULL,
    FOREIGN KEY (projeto_id) REFERENCES CommercialProjects(id),
    FOREIGN KEY (vendedor_id) REFERENCES SalesPeople(id),
    FOREIGN KEY (cota_meta_vendas_id) REFERENCES SalesGoals(id)
);