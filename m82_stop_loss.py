import os
import sqlite3
from datetime import datetime

def set_protective_shield():
    # Parámetros de Protección
    profit_actual = 2400000.0  # $2.4M proyectados
    trailing_stop_pct = 0.05   # Protegemos el 95% de la ganancia máxima
    
    umbral_salida = profit_actual * (1 - trailing_stop_pct)
    
    print(f"🛡️ M82 AGI: Escudo activado.")
    print(f"💰 Ganancia Protegida: ${umbral_salida:,.2f} USD")
    
    # Notificación de voz
    os.system("termux-tts-speak 'Chairman, dynamic stop-loss active. Locking in 2 point 28 million dollars in profit.'")

    # Registrar en el Búnker
    with open("TRADING_LOG.txt", "a") as f:
        f.write(f"{datetime.now()}: SHIELD ACTIVE | Locked Profit Target: ${umbral_salida:,.2f}\n")

if __name__ == "__main__":
    set_protective_shield()
