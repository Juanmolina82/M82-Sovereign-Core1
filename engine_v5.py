import yfinance as yf
import requests
from datetime import datetime
import time

# --- CONFIGURACIÓN SOBERANA ---
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "1020305418"

def send_report():
    try:
        brent = yf.Ticker("BZ=F").fast_info['last_price']
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        mensaje = (
            f"🏛️ **M82 SOVEREIGN CORE — V6.1**\n"
            f"📅 {ahora}\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"🌍 BRENT: ${brent:,.2f}\n"
            f"⚔️ STATUS: IA PLATAFORM ACTIVE\n"
            "🛡️ *Molina Global Infrastructure*"
        )
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                     json={"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"})
        print(f"[{ahora}] Reporte enviado exitosamente.")
    except Exception as e:
        print(f"Error en el pulso: {e}")

if __name__ == "__main__":
    send_report()
