# Used for reading generic CSV's of trades so no manual input is required
# Add Input for trade to be read and saved through csv
import sqlite3
import os

def import_trades_from_csv():
    file_path = input("Enter path to CSV file: ").strip()

    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            cursor.execute('''
                INSERT INTO trades (
                    user, symbol, entry, exit, leverage, fees,
                    capitial, pnl, date, risk, direction, r_multiples
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                row.get('user'),
                row.get('symbol'),
                float(row.get('entry', 0)),
                float(row.get('exit', 0)),
                float(row.get('leverage', 0)),
                float(row.get('fees', 0)),
                float(row.get('capitial', 0)),
                float(row.get('pnl', 0)),
                row.get('date'),
                float(row.get('risk', 0)),
                row.get('direction'),
                float(row.get('r_multiples', 0))
            ))

    conn.commit()
    print("Trades imported successfully!")


conn = sqlite3.connect('trades.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS trades (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user TEXT,
               symbol TEXT,
               entry REAL,
               exit REAL,
               leverage REAL,
               fees REAL,
               capitial REAL,
               pnl REAL,
               date TEXT,
               risk REAL,
               direction TEXT,
               r_multiples REAL)''')
conn.commit()

def save_trade(capital_entry, fees_entry, leverage_entry, entry_entry, exit_entry, direction_combobox, risk_label_entry):
    cursor.execute('''
        INSERT INTO trades(user, symbol, capital, fees, leverage, entry, exit, direction, risk)
        VALUES (?, ?, ?, ?, ?, ?, ?)''',  
        (capital_entry, fees_entry, leverage_entry, entry_entry, exit_entry, direction_combobox, risk_label_entry))
    conn.commit()

    print("File contents saved in database.")

