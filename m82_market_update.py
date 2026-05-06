import os

def final_polish():
    update = """
📊 MARKET PULSE FINAL (POST-CLOSE):
- DJI: 49,910.59 (+1.24%)
- NVDA: $207.83 (+5.77%) -> Alpha Leader.
- DIS: $108.06 (+7.54%) -> Momentum Play.
- NASDAQ: 25,838.94 (+2.02%)
    """
    with open("MEETING_INTEL.txt", "a") as f:
        f.write(update)
    
    print("✅ Reporte actualizado con el cierre del Dow y Nvidia.")

if __name__ == "__main__":
    final_polish()
