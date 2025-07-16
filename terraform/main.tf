provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket        = "${var.project_name}-raw"
  force_destroy = true
}

resource "aws_s3_bucket" "refined_bucket" {
  bucket        = "${var.project_name}-refined"
  force_destroy = true
}

resource "aws_glue_catalog_database" "default_db" {
  name = "${var.project_name}_db"
}

resource "aws_glue_job" "glue_job" {
  name     = var.glue_job_name
  role_arn = var.lab_role_arn

  command {
    name            = "glueetl"
    script_location = "s3://${aws_s3_bucket.raw_bucket.bucket}/scripts/glue-script.py"
    python_version  = "3"
  }

  glue_version       = "3.0"
  number_of_workers  = 2
  worker_type        = "Standard"
}

resource "aws_lambda_function" "trigger_lambda" {
  function_name = var.lambda_function_name
  role          = var.lab_role_arn
  runtime       = "python3.10"
  handler       = "lambda_function.lambda_handler"

  filename         = "${path.module}/lambda/lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda/lambda.zip")

  environment {
    variables = {
      GLUE_JOB_NAME = var.glue_job_name
    }
  }
}

resource "aws_s3_bucket_notification" "notify_lambda" {
  bucket = aws_s3_bucket.raw_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.trigger_lambda.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.trigger_lambda.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.raw_bucket.arn
}
