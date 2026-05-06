import yfinance as yf
from datetime import datetime

def get_m82_intelligence():
    # Definición de activos core
    assets = ["SMCI", "AMD", "NVDA", "GS", "CAT", "ZS=F"]
    
    print(f"📡 M82 AGI: Sincronizando APIs (Fix v2.1)...")
    
    report = f"--- MASTER ARCHITECTURE V3.2: REAL-TIME INTEL ({datetime.now().strftime('%H:%M:%S')}) ---\n"
    
    for ticker in assets:
        try:
            stock = yf.Ticker(ticker)
            # Usamos un método más robusto para obtener el precio actual
            price = stock.history(period="1d")['Close'].iloc[-1]
            
            # Calculamos el estado comparando con la media de 50 días
            history = stock.history(period="50d")
            avg_50 = history['Close'].mean()
            status = "💹 BULLISH" if price > avg_50 else "📉 BEARISH"
            
            line = f"{ticker}: ${price:.2f} | Status: {status}"
            print(f"✅ {line}")
            report += line + "\n"
        except Exception as e:
            print(f"⚠️ Error en {ticker}: {e}")

    with open("REALTIME_MARKET_REPORT.txt", "w") as f:
        f.write(report)
    
    print("\n🛰️ Datos sincronizados y listos en el Búnker.")

if __name__ == "__main__":
    get_m82_intelligence()
