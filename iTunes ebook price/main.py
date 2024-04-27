from flask import Flask, render_template, request
from user_input_data import process_user_input
from search_results import search_results

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entries = request.form['entries']
        if not entries:
            error_message = 'Wprowadź przynajmniej jedną parę autora i tytułu ebooka.'
            return render_template('user_form.html', error_message=error_message)
        
        itunes_data = process_user_input(entries)
        return search_results(itunes_data)

    return render_template('user_form.html')

if __name__ == '__main__':
    app.run(debug=True)
