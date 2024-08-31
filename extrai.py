"""
Projeto Integração DownDetector x Grafana

Autor: Murilo Scheffer
Data: 30/08/2024
Contato: https://www.linkedin.com/in/muriloscheffer/
Git: https://github.com/MuriloSche/downgrafana

Descrição: Este script utiliza a biblioteca Playwright para extrair dados do site DownDetector e armazená-los em um banco de dados PostgreSQL.
Os dados extraídos incluem o nome da empresa e o estado de alerta (danger ou warning). O script limpa a tabela do banco de dados antes de inserir novos dados.

Dependências:
- Playwright
- psycopg2

Instruções:
1. Atualize as informações de conexão com seu banco de dados.    
2. Execute o script para iniciar a extração e armazenamento dos dados.

"""

from playwright.sync_api import sync_playwright
import psycopg2

# Parâmetros de conexão com o banco de dados a partir de variáveis de ambiente
DB_USER = 'postgres'
DB_PASS = 'senha'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'


# Função para salvar os dados no banco de dados
def save_to_postgres(company_name, alert_state):
    try:
        # Conectar ao banco de dados
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        cursor = connection.cursor()
        
        # Inserir os dados na tabela
        insert_query = """INSERT INTO downdetector (nome, status) VALUES (%s, %s)"""
        cursor.execute(insert_query, (company_name, alert_state))
        
        # Confirmar as alterações
        connection.commit()
        print(f"Dados inseridos: Empresa: {company_name}, Estado de Alerta: {alert_state}")
    
    except (Exception, psycopg2.Error) as error:
        print("Erro ao inserir dados no PostgreSQL:", error)
    
    finally:
        # Fechar a conexão
        if connection:
            cursor.close()
            connection.close()

def run(playwright):
    browser = playwright.chromium.launch(headless=False) #Utilizar o Headless como 'True' para que o navegador não seja exibido é bloqueado por um Captcha no site do DownDetector
    page = browser.new_page()
    page.goto("https://downdetector.com.br/")

    # Selecionar elementos com as classes "danger sparkline" e "warning sparkline"
    sparkline_elements = page.query_selector_all('.danger.sparkline, .warning.sparkline')

    # Conectar ao banco de dados para limpar a tabela
    connection = psycopg2.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    cursor = connection.cursor()

    try:
        # Limpar a tabela antes de inserir novos dados
        clear_query = "DELETE FROM downdetector"
        cursor.execute(clear_query)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Erro ao limpar a tabela no PostgreSQL:", error)
    finally:
        # Fechar a conexão
        if connection:
            cursor.close()
            connection.close()
    
    # Extrair e salvar os dados desejados
    for element in sparkline_elements:
        # Extrair o nome da empresa
        company_name = element.evaluate("el => el.closest('.company-card').querySelector('h5').textContent")
        
        # Determinar o estado de alerta (danger ou warning)
        alert_state = "danger" if "danger" in element.get_attribute("class") else "warning"
        
        # Salvar os dados no banco de dados PostgreSQL
        save_to_postgres(company_name, alert_state)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
