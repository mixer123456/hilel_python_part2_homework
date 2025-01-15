from typing import Optional
import requests


def get_token_price(token: str, baseTicker: str = 'USDT') -> Optional[float]:
    url = f"https://min-api.cryptocompare.com/data/price?fsym={token.upper()}&tsyms={baseTicker}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data[baseTicker]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None