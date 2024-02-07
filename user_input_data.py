from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']

        # Walidacja danych - wymagane pola nie mogą być puste
        if not author or not title:
            error_message = 'Wprowadź zarówno autora, jak i tytuł ebooka.'
            return render_template('index.html', error_message=error_message)

        # Przekierowujemy dane do innego widoku
        return redirect(url_for('search_results', author=author, title=title))

    return render_template('index.html')

@app.route('/search-results/<author>/<title>')
def search_results(author, title):
    # Zwracamy komunikat
    return f'Wyszukiwanie dla autora: {author}, tytułu: {title}.'

if __name__ == '__main__':
    app.run(debug=True)