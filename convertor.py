import yfinance as yf

def exchange(fromcurrency, tocurrency, quantity):
    pair = f"{fromcurrency}{tocurrency}=X"
    data = yf.download(pair, period="1d")['Close']
    latest = round(data.iloc[-1] * quantity, 2)
    return latest

def show_currencies():
    currencies = {
        "USD": "United States Dollar",
        "EUR": "Euro",
        "JPY": "Japanese Yen",
        "GBP": "British Pound",
        "INR": "Indian Rupee",
    }
    print("Example Currencies:")
    for abbrev, name in currencies.items():
        print(f"{abbrev}: {name}")

while True:
    print("\nCurrency Exchange Rate Calculator:")
    print("1. Convert two currencies")
    print("2. Help (Show example currencies)")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        fromcurrency = input("Enter the base currency: ").strip().upper()
        tocurrency = input("Enter the target currency: ").strip().upper()
        quantity = float(input("Enter the quantity of the base currency: ").strip())
        
        rate = exchange(fromcurrency, tocurrency, quantity)
        print(f"{quantity} {fromcurrency} = {rate} {tocurrency}")

    elif choice == "2":
        show_currencies()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Please select a valid option.")
