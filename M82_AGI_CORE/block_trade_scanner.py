import datetime

# Umbral para Block Trade: Operaciones > $10M USD
THRESHOLD = 10000000

def monitor_institutional_flow(ticker, volume):
    print(f"--- [M82 BLOCK SCANNER: {datetime.datetime.now()}] ---")
    if volume >= THRESHOLD:
        return f"🚨 ALERTA INSTITUCIONAL: Movimiento masivo detectado en {ticker}. Posible acumulación de Ashmore o Elliott."
    return f"STABLE: Volumen normal en {ticker}."

# Simulación con datos de hoy
print(monitor_institutional_flow("PDVSA 8.375% (CITGO)", 15500000))
print(monitor_institutional_flow("OXY (OCCIDENTAL)", 25000000))
