import pandas as pd
from datetime import datetime

def normalize_data(data):
    results = data.get("results", [])
    if not results:
        raise ValueError("Nenhum dado encontrado na chave 'results'!")

    df = pd.json_normalize(results)

    # Adiciona a data do pregão como coluna
    raw_date = data.get("header", {}).get("date")
    df["data_corrente"] = datetime.strptime(raw_date, "%d/%m/%y").strftime("%Y-%m-%d")
    print(df)

    # Remover as colunas indesejadas se existirem
    columns_to_drop = ["segment", "partAcum"]
    existing_cols = [col for col in columns_to_drop if col in df.columns]
    if existing_cols:
        df = df.drop(columns=existing_cols)
    
    return df
