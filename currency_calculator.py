import requests
from tkinter import messagebox


def handle_error(message):
    messagebox.showerror("Error", message)


def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False


class CurrencyAPIInterface:
    def get_currencies(self):
        pass

    def get_conversion_rate(self, from_currency, to_currency):
        pass


class CurrencyAPI(CurrencyAPIInterface):
    BASE_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest"

    def get_currencies(self):
        url = f"{self.BASE_URL}/currencies.json"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            handle_error(f"Could not fetch currencies: {str(e)}")
            return {}

    def get_conversion_rate(self, from_currency, to_currency):
        url = f"{self.BASE_URL}/v1/currencies/{from_currency}.json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data[from_currency][to_currency]
        except KeyError:
            handle_error(f"Currency conversion from {from_currency} to {to_currency} not available.")
            return None
        except requests.exceptions.RequestException as e:
            handle_error(f"Could not fetch conversion rate: {str(e)}")
            return None


class CurrencyConverter:

    def __init__(self, currency_api: CurrencyAPIInterface):
        self.currency_api = currency_api

    def convert(self, from_currency, to_currency, amount):
        if not is_valid_amount(amount):
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return None

        conversion_rate = self.currency_api.get_conversion_rate(from_currency, to_currency)
        if conversion_rate is not None:
            return float(amount) * conversion_rate
        return None


class CurrencyService:

    def __init__(self, currency_api: CurrencyAPIInterface):
        self.currency_api = currency_api

    def get_currency_codes(self):
        """Return a sorted list of available currency codes."""
        currencies = self.currency_api.get_currencies()
        return sorted(currencies.keys()) if currencies else []
