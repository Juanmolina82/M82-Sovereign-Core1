import pytz
from datetime import datetime
import os

def check_venezuela_pulse():
    # Huso Horario de Venezuela (VET)
    ve_tz = pytz.timezone('America/Caracas')
    ve_time = datetime.now(ve_tz)
    
    # Fecha Crítica: 19 de Junio (Citgo Auction Deadline)
    target_date = datetime(2026, 6, 19, tzinfo=ve_tz)
    days_to_impact = (target_date - ve_time).days
    
    print(f"🇻🇪 M1982 VENEZUELA INTEL | HORA LOCAL: {ve_time.strftime('%H:%M:%S')}")
    print(f"⏳ COUNTDOWN CITGO (19-JUN): {days_to_impact} DÍAS")
    print("----------------------------------------------------------")
    
    # Alerta si estamos en la ventana crítica de Junio
    if days_to_impact <= 45:
        msg = f"Strategic Alert. Citgo collateral auction is in {days_to_impact} days. Monitor Delaware court filings."
        print(f"⚠️ {msg}")
        os.system(f"termux-tts-speak '{msg}'")

if __name__ == "__main__":
    check_venezuela_pulse()

def analyze_us_pressure():
    print("\n🦅 US STATE DEPT WATCH: PLAN MARCO RUBIO")
    print("----------------------------------------------------------")
    print("🗓️ DEADLINE ELECCIONES: Mayo 2027 (Max 12 meses)")
    print("🛡️ ESCUDO CITGO (OFAC): Activo hasta el 19-JUN-2026")
    print("⚠️ RIESGO: Si no hay acuerdo político, el 19-JUN se activa el colateral.")
    
    # Alerta de voz para el News Room
    os.system("termux-tts-speak 'Chairman, US has extended Citgo protection to June 19. The 12-month election clock is ticking.'")

analyze_us_pressure()
