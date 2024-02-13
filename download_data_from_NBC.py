import requests
import datetime

def get_nbp_exchange_rate(currency_code):
    # Pobierz aktualną datę
    current_date = datetime.datetime.now().date().isoformat()

    # Adres URL API NBP dla kursu walut
    url = f'https://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/{current_date}/?format=json'

    try:
        # Wysyłanie zapytania do API
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie, czy nie wystąpiły błędy

        # Parsowanie odpowiedzi JSON
        data = response.json()

        # Wyodrębnianie kursu waluty
        if 'rates' in data and len(data['rates']) > 0:
            rate = data['rates'][0]['mid']
            table_no = data['no']  # Numer tabeli NBP
            return rate, table_no
        else:
            return None, None  # Brak kursu

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas komunikacji z NBP API: {e}')
        return None, None

currency_code = 'USD'
exchange_rate, table_no = get_nbp_exchange_rate(currency_code)

if exchange_rate:
    print(f"Kurs waluty {currency_code} z tabeli NBP ({table_no}): {exchange_rate}")
else:
    print(f"Nie udało się pobrać kursu waluty {currency_code}.")
