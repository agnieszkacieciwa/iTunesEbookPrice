import psycopg2

def save_to_database(author, title, original_price, date, exchange_rate, table_no):
    # Dane dostępowe do bazy PostgreSQL
    db_params = {
        'user': 'agnie',  
        'password': '1234',  
        'host': 'localhost',
        'port': '5432',
        'database': 'ebook_price_exchange'  
    }

    try:
        # Połączenie z bazą danych
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Przeliczenie ceny na PLN
        price_pln = calculate_price_in_pln(original_price, exchange_rate)

        # Zapis do bazy danych
        cursor.execute("""
            INSERT INTO ebook_prices (author, title, original_price, date, exchange_rate, price_pln, table_no)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (author, title, original_price, date, exchange_rate, price_pln, table_no))

        # Zatwierdzenie zmian i zamknięcie połączenia
        connection.commit()
        connection.close()

        print("Dane zapisane do bazy danych.")

    	# Zatwierdzenie zmian i zamknięcie połączenia
   	connection.commit()

    except psycopg2.Error as e:
        print(f'Błąd podczas zapisywania do bazy danych: {e}')

    finally:
        # Zawsze zamknij połączenie, nawet jeśli wystąpi błąd
        connection.close()