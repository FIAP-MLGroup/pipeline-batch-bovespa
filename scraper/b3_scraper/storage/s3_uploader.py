def upload_to_s3(local_file, bucket, s3_prefix, date_str):
    try:
        import boto3
    except ImportError:
        raise ImportError("boto3 não está instalado. Execute com --no-upload ou instale boto3.")

    s3 = boto3.client('s3')
    s3_key = f"{s3_prefix}/date={date_str}/ibov.parquet"
    s3.upload_file(local_file, bucket, s3_key)
    print(f"[✔] Enviado para s3://{bucket}/{s3_key}")