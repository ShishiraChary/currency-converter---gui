import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.exchange_rates = {
            "USD": 1.18,
            "EUR": 1,
            "GBP": 0.86,
            "JPY": 130.32,
            "INR": 88.83
        }

        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = ttk.Label(root, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_currency_combo = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.from_currency_combo.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency_combo.current(0)

        self.to_currency_label = ttk.Label(root, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_currency_combo = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.to_currency_combo.grid(row=2, column=1, padx=10, pady=10)
        self.to_currency_combo.current(1)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_combo.get()
        to_currency = self.to_currency_combo.get()

        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]

        converted_amount = amount * (to_rate / from_rate)
        self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
