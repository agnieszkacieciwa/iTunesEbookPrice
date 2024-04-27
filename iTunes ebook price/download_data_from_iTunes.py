import requests

def search_itunes_api(author, title):
    # Parametry zapytania
    params = {
        'term': f'{author} {title}',
        'entity': 'ebook',
        'limit': 1 # Ograniczenie do 20 wyników
    }

    # Adres URL API iTunes Search
    url = 'https://itunes.apple.com/search'

    try:
        # Wysyłanie zapytania do API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Sprawdzenie, czy nie wystąpiły błędy

        # Parsowanie odpowiedzi JSON
        data = response.json()

        # Wyodrębnianie potrzebnych informacji
        if data['resultCount'] > 0:
            results = data['results']
            formatted_results = []
            for result in results:
                author = result['artistName']
                title = result['trackName']
                release_date = result['releaseDate']
                price = result['price']

                formatted_results.append({
                    'author': author,
                    'title': title,
                    'release_date': release_date,
                    'price': price
                })

            # Przetwarzanie/zwracanie pobranych danych
            return formatted_results
        else:
            return None  # Brak wyników

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas komunikacji z iTunes API: {e}')
        return None