# Pobierz oficjalny obraz Python 3.8
FROM python:3.8

# Ustaw katalog roboczy na /app
WORKDIR /app

# Skopiuj plik zależności do katalogu roboczego
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj pozostałe pliki do katalogu roboczego
COPY . .

# Uruchom aplikację
CMD python user_input_data.py