import tkinter as tk
from tkinter import messagebox
import requests
import os

def lookup_ip():
    ip_address = ip_entry.get().strip()
    if not ip_address:
        messagebox.showwarning("Input Error", "Please enter a valid IP address.")
        return

    api_key = os.getenv("RAPIDAPI_KEY")
    if not api_key:
        messagebox.showerror("API Key Error", "Missing RAPIDAPI_KEY environment variable.")
        return

    url = "https://bigdatacloud-ip-geolocation-v1.p.rapidapi.com/data/country-by-ip"
    querystring = {"ip": ip_address}
    headers = {
        "x-rapidapi-host": "bigdatacloud-ip-geolocation-v1.p.rapidapi.com",
        "x-rapidapi-key": api_key
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            result = f"Country: {data.get('countryName', 'N/A')}
Country Code: {data.get('countryCode', 'N/A')}"
        else:
            result = f"Error: {response.status_code}\n{response.text}"
    except Exception as e:
        result = f"Exception: {str(e)}"

    output_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("IP to Country Lookup")

tk.Label(root, text="Enter IP Address:").pack(pady=5)
ip_entry = tk.Entry(root, width=40)
ip_entry.pack(pady=5)

tk.Button(root, text="Lookup", command=lookup_ip).pack(pady=10)
output_label = tk.Label(root, text="", justify=tk.LEFT)
output_label.pack(padx=10, pady=10)

root.mainloop()
