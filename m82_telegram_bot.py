import os
import requests

def send_to_telegram():
    # --- CONFIGURACIÓN DE CREDENCIALES ---
    TOKEN = "TU_BOT_TOKEN_AQUÍ"
    CHAT_ID = "TU_CHAT_ID_AQUÍ"
    # ------------------------------------
    
    report_path = os.path.expanduser("~/M82_Global_Intelligence/core/MEETING_INTEL.txt")
    
    if not os.path.exists(report_path):
        print("❌ Error: No existe el reporte MEETING_INTEL.txt")
        return

    with open(report_path, "r") as f:
        message = f.read()

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("🚀 Reporte enviado a Telegram exitosamente.")
            os.system("termux-tts-speak 'Chairman, intelligence report broadcasted to Telegram.'")
        else:
            print(f"⚠️ Error al enviar: {response.text}")
    except Exception as e:
        print(f"❌ Fallo de conexión: {e}")

if __name__ == "__main__":
    send_to_telegram()
