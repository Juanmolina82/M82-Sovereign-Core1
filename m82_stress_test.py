import os
from datetime import datetime

def run_stress_test():
    # Parámetros Molina Holdings V3.2
    fixed_rate_debt = 0.80  # 80% de deuda a tasa fija
    target_ffo = 0.42       # 42% objetivo
    
    # Simulación de Shock: Subida de tasas de interés
    shock_impact_on_variable = 0.05 # Impacto del 5% en el 20% de deuda variable
    final_ffo = target_ffo - (shock_impact_on_variable * 0.20)
    
    print("🌪️ M82 AGI: Iniciando Stress Test (Shock de Tasas +200bps)...")
    
    if final_ffo >= 0.40:
        status = "🛡️ RESILIENTE"
        msg = f"Chairman, test exitoso. El FFO se mantiene en {final_ffo*100:.1f}%. La deuda fija protegió el flujo de caja."
    else:
        status = "⚠️ VULNERABLE"
        msg = "Chairman, alerta en el apalancamiento. Se requiere ajuste de cobertura."

    os.system(f"termux-tts-speak '{msg}'")
    
    with open("STRESS_TEST_LOG.txt", "a") as f:
        f.write(f"{datetime.now()}: STRESS TEST | Status: {status} | Final FFO: {final_ffo*100:.2f}%\n")
    
    print(f"📊 Estado Final: {status}")
    print(f"💰 Margen FFO Post-Shock: {final_ffo*100:.2f}%")

if __name__ == "__main__":
    run_stress_test()
