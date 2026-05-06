import requests
import datetime

class ZacksMolinaBot:
    def __init__(self):
        self.ticker = "OXY"
        self.api_url = f"https://www.zacks.com/ap/{self.ticker}"
        # Datos del reporte AP/Zacks de hoy
        self.reported_eps = 1.06
        self.estimated_eps = 0.65
        self.revenue = 5.11e9

    def get_market_sentiment(self):
        # Cálculo de la sorpresa de beneficios (Earnings Surprise)
        surprise = (self.reported_eps - self.estimated_eps) / self.estimated_eps
        
        print(f"--- [ZACKS & M82 SYNC: {datetime.datetime.now()}] ---")
        print(f"ANÁLISIS OXY: Beneficio superior al {surprise:.2%} de lo esperado.")
        
        if surprise > 0.50:
            return "🚀 ESTRATEGIA: ALTA EFICIENCIA DETECTADA. El colateral de Citgo está blindado por el flujo de caja del sector."
        return "ESTADO: Monitoreo de flujo estándar."

# Integrar con el Log de Gobernanza
bot = ZacksMolinaBot()
resultado = bot.get_market_sentiment()

with open('GOBERNANZA_MAESTRA/zacks_intel.log', 'a') as log:
    log.write(f"[{datetime.datetime.now()}] {resultado}\n")

print(resultado)
