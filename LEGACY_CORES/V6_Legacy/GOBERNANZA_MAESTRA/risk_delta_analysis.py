def calculate_risk_drop(current_risk, settlement_date):
    if settlement_date == "2026-06-19":
        # Caída drástica proyectada del 45% en la prima de riesgo
        new_risk = current_risk * 0.55 
        return f"ALERTA M82: Riesgo País cae a {new_risk}. EL GRIFO ESTÁ ABIERTO."
    return "Esperando resolución de colateral."

print(calculate_risk_drop(2500, "2026-06-19"))
