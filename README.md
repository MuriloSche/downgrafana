# Integração DownDetector x Grafana

**Autor:** Murilo Scheffer  
**Data:** 30/08/2024     
**Contato:** https://www.linkedin.com/in/muriloscheffer/          
**Git:** https://github.com/MuriloSche/downgrafana          

**Aviso de Responsabilidade:** 
Este código é disponibilizado para fins educacionais e de uso responsável. Ao utilizá-lo, é fundamental que você tome precauções para não sobrecarregar o site DownDetector ou infringir seus termos de uso. Não assumo qualquer responsabilidade por danos, sobrecargas, bloqueios ou qualquer outro problema que possa surgir do uso inadequado deste código. Por favor, utilize-o com consciência e respeito aos recursos e limites de requisições do site.

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

   - Crie um novo **Dashboard**.
   - Adicione uma nova **Vizualização**.
   ![image](https://github.com/user-attachments/assets/e7b521f9-0f77-4d42-a0c8-d25d7633c97f)
   - Selecione a Base de dados adicionada anteriormente.
   ![image](https://github.com/user-attachments/assets/ef4c4874-ce00-41fa-af5e-4b2d90acb0d7)
   - Configure conforme a imagem.
   ![image](https://github.com/user-attachments/assets/9147be75-06c2-4596-bef6-95c7eccce20d)
   ![image](https://github.com/user-attachments/assets/1597a32c-3eff-401b-8b38-bf6ce46b9800)
   ![image](https://github.com/user-attachments/assets/d8def099-1c49-4bbe-b55a-1238813e5770)


### Aqui são somente ideias, personalize como preferir. 
### Resultado Final
![image](https://github.com/user-attachments/assets/53871788-3a57-445a-9937-c54d2737f837)



     
## Agendamento de Execução
Para garantir a atualização contínua dos dados, o script deve ser executado automaticamente em intervalos regulares. Recomenda-se o uso de uma ferramenta de agendamento como cron no Linux ou o Agendador de Tarefas no Windows. A frequência recomendada é de 1 hora ou mais para evitar sobrecarregar o site DownDetector com requisições excessivas.
