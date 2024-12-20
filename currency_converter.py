def currency_converter(amount, from_currency, to_currency):
    # Exchange rates (hardcoded for now, can be dynamic using an API)
    rates = {
        ("INR", "USD"): 1 / 80,
        ("USD", "INR"): 80,
        ("INR", "EUR"): 1 / 90,
        ("EUR", "INR"): 90,
        ("INR", "GBP"): 1 / 110,
        ("GBP", "INR"): 110,
    }

    # Normalize currency codes to uppercase
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # Conversion logic
    if (from_currency, to_currency) in rates:
        return round(amount * rates[(from_currency, to_currency)], 2)
    else:
        return "Invalid currency conversion pair."

try:
    # User inputs
    currency = float(input("Enter the amount to be converted: "))
    if currency <= 0:
        print("Amount must be positive.")
    else:
        from_currency = input("Enter the currency to be converted from: ")
        to_currency = input("Enter the currency to be converted to: ")
        # Conversion result
        result = currency_converter(currency, from_currency, to_currency)
        print(f"Converted amount: {result}" if isinstance(result, float) else result)
except ValueError:
    print("Invalid input! Please enter a numeric value for the amount.")
