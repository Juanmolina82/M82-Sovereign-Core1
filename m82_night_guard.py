
def check_jpm_anchor():
    jpm_floor = 305.00 # Media de 200 días validada por el Chairman
    stock = yf.Ticker("JPM")
    current = stock.history(period="1d")['Close'].iloc[-1]
    if current > jpm_floor:
        print(f"✅ JPM ANCHOR: Stable at ${current:.2f} (Above 200-DMA)")
    else:
        print(f"⚠️ JPM ALERT: Anchor level testing support.")

check_jpm_anchor()
