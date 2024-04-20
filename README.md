# Learning licence MCQ API

## Introduction
This is a Flask server application that serves multiple-choice questions (MCQs) from a `mcq_data.json` file. It also implements rate limiting for API requests and provides CORS (Cross-Origin Resource Sharing) support.

## Technologies Used
- Python 3.x
- Flask
- Flask-Limiter
- Flask-CORS

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/learning-licence-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd learning-licence-api
    ```

3. Install dependencies:

    ```bash
    pip install -r requirement.txt
    ```

## Project Structure
- **`app.py`**: Server app which is runs the server code.
- **`mcq_data.json`**: Server app which is the entry point to the server
- **`requirement.txt`**: Holds the dependencies for the project.

## Usage

### Server
1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Once the server is running, you can access the following endpoints:

    - `GET /`: Checks if the server is running. Returns `{'status': 'OK'}` if the server is running successfully.
    - `GET /getMCQ`: Returns a JSON response containing 10 randomly selected MCQs from the data file.
    - `GET /resource/<filename>`: Serves static files located in the `resource` directory.

### Rate Limiting

- The `/getMCQ` endpoint has a rate limit of 5 requests per 1 minute by default.
- If the rate limit is exceeded, a `429 Too Many Requests` response will be returned with a message indicating the rate limit policy.

### Error Handling

- **404 Not Found**: If a requested endpoint does not exist, a `404 Not Found` response will be returned.
- **429 Too Many Requests**: If the rate limit is exceeded, a `429 Too Many Requests` response will be returned.

## Contributors
[Ajinkya Bhushan](https://github.com/ajinkya213)

## Acknowledgements
- Special thanks to [Parivahan Sewa](https://parivahan.gov.in/parivahan/) for providing the question-bank in public domain.