# Calculate Ebook Prices Project
This application allows users to query the prices of ebooks in Polish złoty (PLN) based on their release date for a given list of authors and titles. The obtained data is stored in a database, including information about the exchange rate and the table number from which it originates.

## Introduction
The main goal is to determine the ebook price in PLN for a specific date, given a list of authors and titles. The data is fetched by querying the iTunes Search API for ebook details and the NBP API for exchange rates.

## Technologies
- `Python`
- `Flask`
- `PostgreSQL`
- `Docker`
- Other dependencies (install using `pip install -r requirements.txt`)

## How It Works
1. The application sends queries to the iTunes Search API to fetch ebook details.
2. Exchange rates are obtained from the NBP API.
3. The obtained data is organized and stored in a PostgreSQL database.
4. The output is structured according to the specified format.

## APIs Used
- iTunes Search API
- NBP API

## Data Formats 

### Data Input
The input data consists of a list of authors and titles in the following format:
```arduino
"Agatha Christie","The Mysterious Affair at Styles"
"Agatha Christie","The Secret Adversary"
"Agatha Christie","And Then There Were None"
"Agatha Christie","Murder on the Orient Express"
"Agatha Christie","The Murder of Roger Ackroyd"
"Agatha Christie","Death on the Nile"
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
  },
  {
    "name": "Agatha Christie",
    "title": "Murder on the Orient Express",
    "curr": "USD",
    "price": 2.99,
    "date": "2020-04-30",
    "fromNBP": {
      "rate": 3.1288,
      "pricePLN": 9.355112,
      "tableNo": "51/A/NBP/2012"
    }
  }
]
```

## BPMN Diagram

![bPMNDiagram(1)](https://github.com/agnieszkacieciwa/iTunesEbookPrice/assets/88035266/ee630a54-3b9d-4d35-868b-ab9185aa9a35)


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

