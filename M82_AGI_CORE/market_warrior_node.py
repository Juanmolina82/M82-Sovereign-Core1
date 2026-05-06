import json
import datetime

def sync_all_streams():
    # Data de OXY (Zacks) + Data de Crudo (Reuters/Dow Jones)
    market_state = {
        "brent_price": 109.87,
        "wti_price": 102.27,
        "oxy_eps_surprise": 0.63,
        "geopolitics": "Project Freedom Active",
        "citgo_deadline": "2026-06-19"
    }
    
    print(f"--- [M82 TOTAL SYNC: {datetime.datetime.now()}] ---")
    print(f"BRENT @ {market_state['brent_price']} | OXY SURPRISE: +63%")
    
    # Lógica de decisión Molina V3.2
    if market_state['brent_price'] < 115 and market_state['oxy_eps_surprise'] > 0.50:
        return "🔥 ESTATUS: ESCENARIO GOLDILOCKS. Petróleo estable + Eficiencia récord. Ejecutar fase de acercamiento a Amber."
    return "MONITORING."

if __name__ == "__main__":
    print(sync_all_streams())
