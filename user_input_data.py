from flask import Flask, render_template, request, redirect, url_for
import requests
import datetime

app = Flask(__name__)

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

def search_results(author, title):
    # Pobierz dane z iTunes API
    itunes_data = search_itunes_api(author, title)
    # Pobierz kurs waluty z NBP API
    currency_code = 'USD'  # Zakładamy, że to jest dla dolara
    exchange_rate, table_no = get_nbp_exchange_rate(currency_code)

    if itunes_data and exchange_rate:
        # Przygotuj dane w oczekiwanym formacie
        formatted_data = [
            {
                "name": itunes_data['author'],
                "title": itunes_data['title'],
                "curr": currency_code,
                "price": itunes_data['price'],
                "date": itunes_data['release_date'],
                "fromNBP": {
                    "rate": exchange_rate,
                    "pricePLN": calculate_price_in_pln(itunes_data['price'], exchange_rate),
                    "tableNo": table_no
                }
            }
        ]
        return render_template('search_results.html', itunes_data=formatted_data)
    else:
        return render_template('search_results.html', itunes_data=None)

if __name__ == '__main__':
    app.run(debug=True)
