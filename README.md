![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![API](https://img.shields.io/badge/API-newsapi-blue)
![Requests](https://img.shields.io/badge/requests-%5E2.25-blue)

# News API Emailer

## Description

This Python script is designed to fetch the latest news articles related to Tesla from an online news API and send them via email. 
It utilizes the `requests` library for API calls and a custom `send_email` function for emailing. 
The script is configurable via environment variables, allowing for secure API key storage and topic customization.

## Installation

1. **Clone the repository:**
   ```
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**
   ```
   cd <project-directory>
   ```

3. **Install dependencies:**
   ```
   pip install requests python-dotenv
   ```

## Configuration

1. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your API key to the `.env` file:
     ```
     API_KEY=your_api_key_here
     ```

2. **Email Function Setup:**
   - Ensure the `send_email` function in `send_email.py` is properly configured with your email server settings.

## Usage

Run the script with the following command:

```
python <script-name>.py
```

The script will fetch the latest news about Tesla and send an email with the news content.

## Requirements

- Python 3.11
- Requests library
- dotenv library

## License

This project is under the MIT License.

