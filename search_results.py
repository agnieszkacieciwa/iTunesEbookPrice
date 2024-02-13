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