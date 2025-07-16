# Infraestrutura do projeto – Terraform

Este diretório contém a definição da **infraestrutura AWS** para o pipeline de ingestão e processamento batch da B3.

## Descrição

O Terraform provisiona os seguintes recursos:

- Buckets S3 para dados brutos e processados.
- AWS Glue Catalog Database.
- AWS Glue Job (referenciando script PySpark no S3).
- AWS Lambda Function para orquestração (opcional).

⚠️ **Obs.:** As IAM Roles necessárias (ex.: LabRole) já devem existir no ambiente. O Terraform apenas referencia esses ARNs – ele **não cria** roles.

---

## Pré-requisitos

- [Terraform](https://developer.hashicorp.com/terraform/downloads) instalado.
- Credenciais AWS configuradas (perfil ou variáveis de ambiente).
- Permissões para criar recursos S3, Glue e Lambda (IAM Roles pré-criadas).

---

## Principais variáveis

- `region`: Região AWS onde os recursos serão criados.
- `project_name`: Prefixo para nomear buckets e recursos.
- `lab_role_arn`: ARN da role IAM já existente no ambiente (ex.: LabRole).
- `glue_script_location`: Caminho S3 para o script PySpark do Glue Job.

Você pode definir essas variáveis via `terraform.tfvars` ou na linha de comando.

---

## Comandos básicos

### Inicializar o projeto

```bash
terraform init
```

### Visualizar o plano de execução

```bash
terraform plan
```

### Aplicar o plano (com auto-approve)

```bash
terraform apply -auto-approve
```

### Exemplo com variáveis

```bash
terraform apply \
  -var="region=us-east-1" \
  -var="project_name=b3-tech-challenge" \
  -var="lab_role_arn=arn:aws:iam::ACCOUNT_ID:role/LabRole" \
  -var="glue_script_location=s3://meu-bucket/scripts/glue-etl-job.py"
```