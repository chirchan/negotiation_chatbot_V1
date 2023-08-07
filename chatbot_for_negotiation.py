import pandas as pd
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import simpledialog, messagebox

# Sample historical data from the current supplier
historical_data = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03'],
    'Price': [100, 110, 120]
}
historical_df = pd.DataFrame(historical_data)

# Sample pricing data from other suppliers
competitive_data = {
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C'],
    'Price': [95, 105, 115]
}
competitive_df = pd.DataFrame(competitive_data)

def to_numeric_date(date_str):
    reference_date = datetime.strptime('2023-07-01', '%Y-%m-%d')
    current_date = datetime.strptime(date_str, '%Y-%m-%d')
    numeric_date = (current_date - reference_date).days
    return numeric_date

def price_prediction_model(historical_df, current_date):
    X = historical_df['Date'].apply(to_numeric_date).values.reshape(-1, 1)
    y = historical_df['Price'].values

    model = LinearRegression()
    model.fit(X, y)

    current_date_value = to_numeric_date(current_date)
    predicted_price = model.predict([[current_date_value]])[0]

    return predicted_price

def competitive_analysis(competitive_df):
    lowest_price = competitive_df['Price'].min()
    return lowest_price

def negotiation_bot(initial_supplier_quote):
    current_date = '2023-07-04'  # Replace with the actual current date
    predicted_price = price_prediction_model(historical_df, current_date)
    lowest_competitor_price = competitive_analysis(competitive_df)

    target_price = max(predicted_price, lowest_competitor_price)

    if initial_supplier_quote <= target_price:
        return f"Negotiation successful! Final price: {initial_supplier_quote}"
    else:
        revised_supplier_quote = simpledialog.askfloat("Revised Price", "Your initial price is not accepted. Please enter a revised price:")
        if revised_supplier_quote is not None:
            if revised_supplier_quote <= target_price:
                return f"Negotiation successful! Final price: {revised_supplier_quote}"
            else:
                return f"Negotiation failed. The revised price is still not acceptable. Target price: {target_price}"
        else:
            return "Negotiation canceled. No revised price provided."

def on_submit():
    try:
        initial_supplier_quote = float(entry.get())
        result = negotiation_bot(initial_supplier_quote)
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value.")

# Create the GUI
root = tk.Tk()
root.title("Negotiation Bot")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter the current supplier quote:")
label.pack()

entry = tk.Entry(frame, width=10)
entry.pack()

submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
