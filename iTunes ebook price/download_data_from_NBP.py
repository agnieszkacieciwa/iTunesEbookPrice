import requests
import datetime

def get_nbp_exchange_rate(currency_code, date):
    # Konwersja daty ze stringa na obiekt datetime
    date = datetime.datetime.fromisoformat(date)

    # Formatowanie daty zgodnie z wymaganiami NBP (RRRR-MM-DD)
    formatted_date = date.strftime('%Y-%m-%d')

    # Adres URL API NBP dla kursu walut na daną datę
    url = f'https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/{formatted_date}/?format=json'

    try:
        # Wysyłanie zapytania do API
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy nie wystąpiły błędy

        # Parsowanie odpowiedzi JSON
        data = response.json()

        # Wyodrębnianie kursu waluty
        if 'rates' in data and len(data['rates']) > 0:
            rate = data['rates'][0]['mid']
            table_no = data.get('no', None)  # Numer tabeli NBP, jeśli istnieje
            return rate, table_no
        else:
            return None, None  # Brak kursu

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas komunikacji z NBP API: {e}')
        return None, None
