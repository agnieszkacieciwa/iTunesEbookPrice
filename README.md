# Calculate Ebook Prices Project
This application allows users to query the prices of ebooks in Polish złoty (PLN) based on their release date for a given list of authors and titles.

## Introduction
The main goal is to determine the ebook price in PLN for a specific date, given a list of authors and titles. The data is fetched by querying the iTunes Search API for ebook details and the NBP API for exchange rates.

## Technologies
- `Python`
- `Flask`
- `PostgreSQL`
- `Docker`
- Other dependencies (install using `pip install -r requirements.txt`)

## How It Works
The application works by taking input from the user in the form of the author and title of the ebook. It then queries the iTunes Store API to fetch information about the ebook, including its price in the iTunes currency. Next, it retrieves the currency exchange rate from the NBP API for the date of the ebook's release. Using this exchange rate, it converts the ebook price to PLN and displays it to the user

## APIs Used
- iTunes Search API
- NBP API

## Data Formats 

### Data Input
The input data consists of a list of authors and titles in the following format:
```arduino
Agatha Christie,The Secret Adversary
Agatha Christie,The Lying Game
```
### Output Structure
The output is structured as follows:
```json
[
  {
    "name": "Agatha Christie",
    "title": "The Lying Game",
    "curr": "USD",
    "price": 16.99,
    "date": "2022-09-08",
    "fromNBP": {
      "rate": 3.1288,
      "pricePLN": 53.158312,
      "tableNo": "51/A/NBP/2012"
    }
]
```


## Usage 
1. Clone the repository:
   ```bash
   git clone https://github.com/agnieszkacieciwa/iTunesEbookPrice.git
   cd iTunesEbookPrice
   ```
2. Build and run the Docker container:
   ```bash
   docker build -t ebook-price-app .
   docker run -it --name ebook-price-app -p 5000:5000 ebook-price-app
   ```
3. Access the application in your web browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

