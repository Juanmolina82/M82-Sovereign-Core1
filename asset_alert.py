import requests
import yfinance as yf
from datetime import datetime

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "1020305418"

def send_bam_alert():
    try:
        bam = yf.Ticker("BAM")
        price = bam.fast_info['last_price']
        ahora = datetime.now().strftime('%H:%M')
        
        mensaje = (
            f"⚠️ **MARKET ALERT — ASSET MANAGEMENT**\n"
            f"📅 {ahora} GMT\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🏦 **JP MORGAN DOWNGRADE:**\n"
            "• ASSET: Brookfield Asset Management (BAM)\n"
            "• TARGET: $72 ➔ $60 (RECORTE CRÍTICO)\n\n"
            f"📉 **PRECIO ACTUAL:** ${price:,.2f}\n"
            "🔍 **INSIGHT:** Wall Street anticipa presión en activos reales. El Core debe monitorear "
            "la exposición a fondos de infraestructura.\n\n"
            "🛡️ *M82 Sovereign Intelligence*"
        )
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                     json={"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"})
        print("Alerta de Brookfield enviada.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_bam_alert()
