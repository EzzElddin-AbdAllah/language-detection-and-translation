# Language Detection and Translation

This project aims to provide language detection and translation capabilities using machine learning techniques. It includes a language detection model trained on a labeled dataset and a translation feature powered by an external translation service.

## Features

- Language Detection: Identify the language of a given text.
- Translation: Translate text from Arabic language to English and vice versa.

## Installation

1. Clone the repository: 
```
git clone https://github.com/EzzElddin-AbdAllah/language-detection-and-translation.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Start the Flask app:
```
python main.py
```

## API Documentation

The API endpoints and their usage are documented in the Postman collection. You can find the collection file in the `postman/` directory. Import the collection into Postman to explore and test the API endpoints.

## Sample Request

To make a sample request to the API using a Python script, you can use the `sample_request.py` script located in the `scripts/` directory. Update the script with the necessary information and execute it to send a request to the API and receive a response.

## Running Tests

The project includes test files to ensure the correctness of the implemented functionality. To run the tests, use the following command:
```
pytest tests/
```




