import requests


def search_itunes_api(author, title):
    # Parametry zapytania
    params = {
        'term': f'{author} {title}',
        'entity': 'ebook',
        'limit': 1  # Ograniczenie do jednego wyniku
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
            result = data['results'][0]
            author = result['artistName']
            title = result['trackName']
            release_date = result['releaseDate']
            price = result['collectionPrice']

            # Przetwarzanie/zwracanie pobranych danych
            return {
                'author': author,
                'title': title,
                'release_date': release_date,
                'price': price
            }
        else:
            return None  # Brak wyników

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas komunikacji z iTunes API: {e}')
        return None

itunes_data = search_itunes_api(author, title)

if itunes_data:
    print("Dane z iTunes API:")
    print(f"Autor: {itunes_data['author']}")
    print(f"Tytuł: {itunes_data['title']}")
    print(f"Data wydania: {itunes_data['release_date']}")
    print(f"Cena: {itunes_data['price']}")
else:
    print("Brak wyników z iTunes API.")
