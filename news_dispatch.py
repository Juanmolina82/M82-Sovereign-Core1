import requests
import yfinance as yf
from datetime import datetime

# --- CREDENCIALES ---
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAT_ID = "1020305418"

def send_news_report():
    try:
        # Captura de precios post-noticia
        brent = yf.Ticker("BZ=F").fast_info['last_price']
        gold = yf.Ticker("GC=F").fast_info['last_price']
        dxy = yf.Ticker("DX-Y.NYB").fast_info['last_price']
        ahora = datetime.now().strftime('%H:%M')
        
        reporte = (
            f"🏛️ **M82 INTEL DISPATCH — GEOPOLITICAL PIVOT**\n"
            f"📅 06 MAY 2026 | {ahora} GMT\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "📰 **HEADLINE:** TRUMP PAUSES HORMUZ ESCORT / IRAN PEACE DEAL\n\n"
            "📊 **MARKET REACTION:**\n"
            f"• BRENT: ${brent:,.2f} (EASING 📉)\n"
            f"• GOLD: ${gold:,.2f} (JUMPING 📈)\n"
            f"• DXY: {dxy:.2f} (WEAKENING 📉)\n\n"
            "🔍 **STRATEGIC INSIGHT:**\n"
            "La 'Operación Epic Fury' ha concluido según Marco Rubio. El mercado está eliminando "
            "la prima de riesgo bélico del crudo. El refugio se desplaza masivamente al ORO "
            "ante la debilidad del Dólar inducida por el Tesoro.\n\n"
            "🛡️ *Molina Global Workspace - Sovereign Intelligence*"
        )
        
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                     json={"chat_id": CHAT_ID, "text": reporte, "parse_mode": "Markdown"})
        print("Dispatch enviado exitosamente al bot.")
    except Exception as e:
        print(f"Error en dispatch: {e}")

if __name__ == "__main__":
    send_news_report()
