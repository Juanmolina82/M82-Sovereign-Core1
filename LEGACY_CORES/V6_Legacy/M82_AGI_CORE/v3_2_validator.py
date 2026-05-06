import json

ARCH_LIMITS = {
    "max_leverage": 4.5,
    "min_ebitda_margin": 0.60,
    "hurdle_rate": 0.08,
    "fixed_rate_hedge": 0.80
}

def check_proposal(leverage, ebitda_margin):
    if leverage > ARCH_LIMITS["max_leverage"]:
        return "⚠️ ALERTA: Apalancamiento excede 4.5x. Violación V3.2."
    if ebitda_margin < ARCH_LIMITS["min_ebitda_margin"]:
        return "⚠️ ALERTA: Margen EBITDA por debajo del 60%. Riesgo operativo."
    return "✅ PROPUESTA ALINEADA CON ARQUITECTURA V3.2 FINAL."

# Test de estrés con los datos de Citgo/PDVSA
print(check_proposal(4.2, 0.65))
