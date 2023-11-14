
# analyser.py
import pandas as pd
import re
import datetime

def extract_strike_rates():
    """
    Extracts strike rates from an Excel file with stock messages.
    The Excel file is expected to be named with today's date.
    """
    print("ANALYSER RUNNING")
    today = datetime.date.today()
    file_path = f"D:\Telegram Stocks\messages_{today}.xlsx"

    try:
        df = pd.read_excel(file_path, sheet_name='Sheet1')
        messages = df.iloc[:, 2].tolist()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    pe_strike_rates = []
    ce_strike_rates = []

    for message in messages:
        buy_value = re.findall(r"\d{4,5}", message)
        if re.search(r'PE|WEAK|PUT', message, re.IGNORECASE):
            pe_strike_rates.append(int(buy_value[0]))
        elif re.search(r'CE|CALL|ABOVE', message, re.IGNORECASE):
            ce_strike_rates.append(int(buy_value[0]))

    return pe_strike_rates, ce_strike_rates

if __name__ == "__main__":
    pe_rates, ce_rates = extract_strike_rates()
    print("PE Strike Rates:", pe_rates)
    print("CE Strike Rates:", ce_rates)
