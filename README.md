# Tech Challenge - Pipeline Batch Bovespa

Este repositório contém a implementação do **pipeline batch** para ingestão e processamento de dados do índice IBOV da B3 na AWS, atendendo aos requisitos do Tech Challenge.

---

## Estrutura do repositório

```
.
├── scraper/ # Script Python para scraping e ingestão no S3
├── terraform/ # Infraestrutura como código (AWS) com Terraform
````

## Diretórios principais

### 📂 [`scraper/`](./scraper/)

- Script Python modular para:
  - Fazer scraping dos dados do IBOV a partir da API da B3.
  - Salvar os dados em formato Parquet, particionado por data.
  - Enviar os dados para o bucket S3 (camada raw).

- Inclui:
  - README com instruções para ambiente virtual, dependências e execução.
  - Código organizado em pacotes para facilitar manutenção.

➡️ [Acessar o README do scraper](./scraper/README.md)

### 📂 [`terraform/`](./terraform/)

- Infraestrutura como código para:
  - Buckets S3 (raw e refined).
  - Glue Catalog Database.
  - Glue Job (referenciando o script PySpark no S3).
  - Lambda Function para orquestração (opcional).

- Inclui:
  - Variáveis para parametrização.
  - README com instruções de uso.

➡️ [Acessar o README do terraform](./terraform/README.md)

## Observações

- O script PySpark do Glue (para ETL) deve ser desenvolvido separadamente (ex.: no AWS Glue Studio) e salvo no S3 para ser referenciado no Terraform.
- IAM Roles necessárias (como `LabRole`) devem já existir no ambiente. O Terraform apenas referencia esses ARNs.


## Configuração do AWS Cli

O LAB fornecido no AWS Accademy possui uma instância interna que pode ser utilizada para execução do AWS Cli ou outras ferramentas já embarcadas.

Para utilização de ferramentas mais avançadas como terraform, é possível realizar o acesso ao LAB localmente realizando o seguinte procedimento.

* Inicie o LAB, clicando em "Start Lab".
* Na instância interna do LAB, verifique as credenciais utilizadas:

    ```bash
    cat .aws/credentials
    ```

    É esperado que o conteúdo do arquivo seja similar a esse:

    ```bash
    [default]
    aws_access_key_id = ASIA2VJ4PBHURF2PAJ5B
    aws_secret_access_key = 0FsjtSw7Sw6CLnjL/xa8b37gwgNi1T4IThMlu3ZS
    aws_session_token = IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQDaRflHDzVyODbLl7EjXNMj8emPPfqahSd4XEthKGrxEwIgGdsomv/+mqJvWCPhG0r9HrwQ
    ```

* Na sua instância local exporte as seguintes variáveis de ambiente, substituindo os valores de acordo com o resultado do comando anterior:

    ```bash
    export AWS_ACCESS_KEY_ID=<aws_access_key_id>
    export AWS_SECRET_ACCESS_KEY=<aws_secret_access_key>
    export AWS_SESSION_TOKEN=<aws_session_token>
    ```

* Esse procedimento deverá ser realizado toda vez que o LAB for reiniciado.