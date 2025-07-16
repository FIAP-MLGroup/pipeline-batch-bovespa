output "raw_bucket_name" {
    value = aws_s3_bucket.raw_bucket.bucket
}

output "refined_bucket_name" {
    value = aws_s3_bucket.refined_bucket.bucket
}

output "lambda_function_name" {
    value = aws_lambda_function.trigger_lambda.function_name
}

output "glue_job_name" {
    value = aws_glue_job.glue_job.name
}

output "glue_catalog_database" {
    value = aws_glue_catalog_database.default_db.name
}
