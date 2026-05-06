def identify_partners():
    targets = [
        {"firm": "Nashville Energy Wealth", "AUM": "350M", "focus": "Oil & Gas"},
        {"firm": "Chattanooga Global Partners", "AUM": "420M", "focus": "Infrastructure"},
        {"firm": "Knoxville Capital Advisors", "AUM": "280M", "focus": "Legacy Estates"}
    ]
    for t in targets:
        print(f"TARGET DETECTED: {t['firm']} | AUM: {t['AUM']} | FIT: HIGH")

identify_partners()
