import argparse
import datetime

from b3_scraper.fetcher.b3_client import fetch_ibov_data
from b3_scraper.fetcher.parser import normalize_data
from b3_scraper.storage.parquet_writer import save_parquet
from b3_scraper.storage.s3_uploader import upload_to_s3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="./data/raw")
    parser.add_argument("--s3-bucket", default=None)
    parser.add_argument("--s3-prefix", default="raw-data")
    parser.add_argument("--no-upload", action="store_true")
    args = parser.parse_args()

    date_str = datetime.datetime.today().strftime("%Y-%m-%d")

    print("[*] Buscando dados do IBOV...")
    json_data = fetch_ibov_data()
    df = normalize_data(json_data)

    if df.empty:
        print("[!] Nenhum dado retornado.")
        return

    local_file = save_parquet(df, args.output_dir, date_str)

    if not args.no_upload and args.s3_bucket:
        upload_to_s3(local_file, args.s3_bucket, args.s3_prefix, date_str)

if __name__ == "__main__":
    main()
