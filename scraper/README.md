# B3 IBOV Data Scraper

Este script realiza o **scraping dos dados do pregão da B3 (IBOV)** consumindo a API pública disponibilizada no site da B3.  
Ele extrai os dados em formato JSON, transforma em um DataFrame Pandas, e salva em **formato Parquet particionado por data** (YYYY-MM-DD).  

O script também pode opcionalmente **enviar os dados diretamente para um bucket S3**, cumprindo o requisito de ingestão bruta do pipeline Batch (Requisitos 1 e 2 do desafio).

---

## Configuração e Execução

### Criar venv e instalar dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Rodar local e salvar Parquet

```bash
python -m b3_scraper --no-upload
```

### Rodar enviando para S3

```bash
python -m b3_scraper --s3-bucket MEU_BUCKET_RAW
```
