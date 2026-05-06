import yfinance as yf
import pandas as pd
import requests
from datetime import datetime
import os

ASSETS = ["BZ=F", "GC=F", "DX-Y.NYB", "CL=F"]
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "1020305418"

def analyze_market():
    report = "🏛️ **M82 BIG DATA ANALYSIS — V6.2**\n\n"
    data_to_save = {}
    
    for asset in ASSETS:
        ticker = yf.Ticker(asset)
        hist = ticker.history(period="30d")
        current = hist['Close'].iloc[-1]
        change = ((current - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
        vol = hist['Close'].std()
        
        status = "📈 BULLISH" if change > 0 else "📉 BEARISH"
        report += f"🔹 **{asset}**: ${current:,.2f} ({change:+.2f}%)\n"
        report += f"   *Volatilidad:* {vol:.2f} | {status}\n\n"
        data_to_save[asset] = current

    # Guardar en Big Data Storage
    df = pd.DataFrame([data_to_save])
    df['timestamp'] = datetime.now()
    log_file = "data/raw/market_history.csv"
    df.to_csv(log_file, mode='a', header=not os.path.exists(log_file), index=False)
    
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                 json={"chat_id": CHAT_ID, "text": report, "parse_mode": "Markdown"})
    print("Análisis y almacenamiento completado.")

if __name__ == "__main__":
    analyze_market()
