variable "region" {
    default = "us-east-1"
}

variable "project_name" {
    default = "b3-tech-challenge"
}

variable "glue_job_name" {
    default = "b3-glue-job"
}

variable "lambda_function_name" {
    default = "b3-trigger-lambda"
}

#############################################################################
# Alterar o account_id de acordo com o ambiente onde o código será aplicado #
#############################################################################
variable "lab_role_arn" {
    description = "ARN da IAM Role já existente no ambiente (LabRole)"
    default     = "arn:aws:iam::732955609577:role/LabRole"
}