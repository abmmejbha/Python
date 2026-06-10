from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., Taka): ").upper()

print(from_currency, "To", to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print("Converted amount:", result)