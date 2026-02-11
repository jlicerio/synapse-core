import pandas as pd
import sys

filename = "AV6_Strategy_[Backtest]_CME_MINI_MNQ1!_2026-02-09.xlsx"

try:
    df = pd.read_excel(filename, sheet_name="Performance", header=None)
    
    # Iterate through ALL rows and cols
    for index, row in df.iterrows():
        row_str = " ".join([str(val) for val in row if pd.notna(val)])
        
        if "Net Profit" in row_str:
            print(f"NET PROFIT ROW ({index}): {row_str}")
        if "Profit Factor" in row_str:
            print(f"PROFIT FACTOR ROW ({index}): {row_str}")
        if "Max Drawdown" in row_str:
            print(f"MAX DRAWDOWN ROW ({index}): {row_str}")
        if "Total Closed Trades" in row_str:
            print(f"TOTAL TRADES ROW ({index}): {row_str}")
            
except Exception as e:
    print(f"Error: {e}")
