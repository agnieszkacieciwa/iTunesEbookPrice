def calculate_price_in_pln(original_price, exchange_rate):
    # Przeliczenie ceny na podstawie kursu walut
    return round(original_price * exchange_rate, 2)
