import os
from datetime import datetime

def log_insider_activity():
    executive = "David Solomon (CEO GS)"
    action = "SELL"
    value = 3229543.00
    remaining_shares = 153433
    filing_date = "2026-05-01"
    
    print(f"🕵️ M82 AGI: Rastreada actividad de Insider SEC en Goldman Sachs")
    print(f"💼 {executive} liquidó ${value:,.2f} USD")
    
    # Análisis de retención
    retention_percent = (remaining_shares / (remaining_shares + 3470)) * 100
    print(f"📊 Retención de Solomon: {retention_percent:.2f}% (Señal: ESTABLE)")

    with open("INSIDER_TRADING_LOG.txt", "a") as f:
        f.write(f"{datetime.now()}: {executive} | {action} | ${value:,.2f} | Retention: {retention_percent:.2f}%\n")
    
    os.system("termux-tts-speak 'Chairman, insider sale by Solomon registered. Impact: Negligible. He retains over 97 percent of his stake.'")

if __name__ == "__main__":
    log_insider_activity()
