import os

def save_parquet(df, output_dir, date_str):
    import pyarrow  # garante erro útil se não estiver instalado
    output_path = os.path.join(output_dir, f"date={date_str}")
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, "ibov.parquet")
    df.to_parquet(file_path, index=False)
    print(f"[✔] Dados salvos: {file_path}")
    return file_path