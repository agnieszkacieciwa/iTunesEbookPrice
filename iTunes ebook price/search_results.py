from flask import render_template
from calculate_ebook_price import calculate_price_in_pln
from download_data_from_NBP import get_nbp_exchange_rate

def search_results(itunes_data):
    currency_code = 'USD'  # Zakładamy, że to jest dla dolara
    formatted_data = []

    for item in itunes_data:
        author = item['author']
        title = item['title']
        price = item['price']
        release_date = item['release_date']

        exchange_rate, table_no = get_nbp_exchange_rate(currency_code, release_date)

        if exchange_rate:
            price_pln = calculate_price_in_pln(price, exchange_rate)
            formatted_data.append({
                "name": author,
                "title": title,
                "curr": currency_code,
                "price": price,
                "date": release_date,
                "fromNBP": {
                    "rate": exchange_rate,
                    "pricePLN": price_pln,
                    "tableNo": table_no
                }
            })
        else:
            print(f"Nie udało się pobrać kursu waluty USD na datę wydania ebooka ({release_date}).")

    return render_template('search_results.html', itunes_data=formatted_data)
