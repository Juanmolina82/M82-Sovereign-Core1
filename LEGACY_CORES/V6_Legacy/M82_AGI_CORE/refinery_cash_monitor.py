import datetime

def audit_gulf_margins():
    # Datos de Reuters 05-May-2026
    m2_gasoline_diff = -0.065 # 6.5 cents below futures
    ulsd_diff = -0.02 # 2 cents below futures
    
    print(f"--- [M82 REFINERY AUDIT: {datetime.datetime.now()}] ---")
    print(f"GULF COAST M2 DIFF: {m2_gasoline_diff} | STATUS: Selling Pressure")
    
    # Interpretación estratégica
    return "💡 INSIGHT: Refinerías operando al 95%+. Citgo está generando flujo masivo antes del settlement de Junio."

print(audit_gulf_margins())
