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

