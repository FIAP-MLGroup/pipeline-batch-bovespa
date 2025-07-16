import requests

B3_IBOV_API_URL = (
    "https://sistemaswebb3-listados.b3.com.br/"
    "indexProxy/indexCall/GetPortfolioDay/"
    "eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjEifQ=="
)

def fetch_ibov_data():
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(B3_IBOV_API_URL, headers=headers)
    resp.raise_for_status()
    return resp.json()