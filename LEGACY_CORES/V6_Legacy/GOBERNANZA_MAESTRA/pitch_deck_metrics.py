def generate_pitch_stats():
    lpl_yield = 5.75  # Max yield observed in captures
    molina_hurdle = 8.00
    spread = molina_hurdle - lpl_yield
    
    print(f"--- [PITCH DECK DATA SYNC] ---")
    print(f"Competitor Yield: {lpl_yield}%")
    print(f"Molina V3.2 Hurdle: {molina_hurdle}%")
    print(f"Competitive Advantage (Spread): +{spread}%")
    print(f"Status: Ready for Tennessee Outreach.")

generate_pitch_stats()
