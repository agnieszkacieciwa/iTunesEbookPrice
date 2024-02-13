from flask import Flask, render_template, request, redirect, url_for
import requests
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']

        if not author or not title:
            error_message = 'Wprowadź zarówno autora, jak i tytuł ebooka.'
            return render_template('index.html', error_message=error_message)

        # Przesyłamy dane do szablonu HTML w przypadku, gdy użytkownik dokonał wyszukiwania
        itunes_data = search_itunes_api(author, title)
        exchange_rate = get_nbp_exchange_rate('USD')  

if __name__ == '__main__':
    app.run(debug=True)

