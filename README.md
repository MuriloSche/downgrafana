# Integração DownDetector x Grafana

**Autor:** Murilo Scheffer  
**Data:** 30/08/2024     
**Contato:** https://www.linkedin.com/in/muriloscheffer/          
**Git:** https://github.com/MuriloSche/downgrafana          

## Descrição

O projeto **Integração DownDetector x Grafana** visa integrar dados de estado de alerta de empresas do site [DownDetector](https://downdetector.com.br/) com o painel de visualização de dados do [Grafana](https://grafana.com/). Utilizando técnicas de web scraping, o script extrai informações sobre o status de alerta (danger ou warning) e armazena esses dados em um banco de dados PostgreSQL. O Grafana é então configurado para visualizar esses dados em um painel, proporcionando uma visão clara e organizada do estado de alerta atual.

## Objetivo

Fornecer uma solução automatizada para monitorar e visualizar o estado de alerta das empresas listadas no DownDetector, permitindo uma análise rápida e eficiente através de dashboards personalizados no Grafana.

## Requisitos

### Software

- **Python 3.x**: Versão 3.7 ou superior recomendada para garantir compatibilidade com as bibliotecas utilizadas.
- **Playwright**: Biblioteca para realizar web scraping do site DownDetector.
- **psycopg2**: Biblioteca para interagir com o banco de dados PostgreSQL.
- **PostgreSQL**: Banco de dados para armazenar os dados extraídos do DownDetector.
- **Grafana**: Para visualização dos dados extraídos. Deve ser configurado para conectar-se ao banco de dados PostgreSQL e criar painéis de visualização.

### Hardware/Infraestrutura

- **Servidor para PostgreSQL**: Pode ser local ou remoto.
- **Servidor para Grafana**: Pode ser local ou remoto.
- **Máquina para Execução do Script**: Onde o script Python será executado. Pode ser uma máquina local ou um servidor na nuvem.

## Web Scraping

O script utiliza a biblioteca Playwright para realizar web scraping do site DownDetector. A abordagem headless é utilizada para evitar a solicitação de CAPTCHA durante a execução do script. A coleta de dados é feita das seguintes maneiras:

- **Extração de Dados**: O script extrai o nome da empresa e o estado de alerta das empresas listadas com as classes CSS `danger sparkline` e `warning sparkline`.
- **Armazenamento**: Os dados extraídos são armazenados em uma tabela PostgreSQL para posterior visualização no Grafana.

## Uso do Banco de Dados

Foi utilizado o PostgreSQL para armazenar os dados devido à sua robustez e flexibilidade. Você pode adaptar o código para usar outro banco de dados, se preferir. Basta criar uma tabela no banco com o nome `downdetector` com duas colunas:

- **nome**: O nome da empresa.
- **status**: O estado de alerta da empresa, que pode ser "danger" (crítico) ou "warning" (aviso).

## Configuração do Grafana

### Adicionar Fonte de Dados PostgreSQL

1. No Grafana, acesse **Configuration** > **Data Sources**.
2. Clique em **Add data source** e selecione **PostgreSQL**.
3. Preencha as informações de conexão:
   - **Host**: `localhost:5432`
   - **Database**: `postgres`
   - **User**: `postgres`
   - **Password**: `your_password`

### Criar um Painel de Tabela

1. Crie um novo painel no **Dashboard**.
2. Adicione uma nova consulta SQL para a tabela `downdetector`:

   ```sql
   SELECT * FROM downdetector
