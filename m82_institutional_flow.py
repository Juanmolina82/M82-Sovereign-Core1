import os
from datetime import datetime

def log_institutional_signal():
    ticker = "GS.N (Goldman Sachs)"
    imbalance_shares = 87470
    side = "BUY"
    source = "LSEG Workspace"
    
    print(f"📡 M82 AGI: Detectada señal institucional en {ticker}")
    print(f"🔥 Imbalance: {imbalance_shares} acciones al BUY SIDE")
    
    # Notificación táctica
    os.system("termux-tts-speak 'Chairman, massive buy imbalance detected in Goldman Sachs. Institutional confidence is peaking.'")

    with open("INSTITUTIONAL_SIGNALS.txt", "a") as f:
        f.write(f"{datetime.now()}: {ticker} | {side} Imbalance: {imbalance_shares} | Source: {source}\n")
    
    print("✅ Señal sincronizada con el búnker.")

if __name__ == "__main__":
    log_institutional_signal()
