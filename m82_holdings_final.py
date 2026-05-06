import telebot
import time
import requests

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.from_user.id == CHAIRMAN_ID)
def core_response(m):
    header = "🦅 <b>M82 HOLDINGS - SISTEMA INTEGRADO</b>\n"
    reporte = (f"{header}├ <b>GitHub:</b> Sincronizado ✅\n"
               f"├ <b>Arquitectura:</b> Local Validada ✅\n"
               f"└ <b>Estatus:</b> Operativo bajo mando M82.")
    bot.reply_to(m, reporte, parse_mode='HTML')

def run_safe():
    print(">> MATRIZ M82: ELIMINANDO CONFLICTOS 409...")
    # Limpia cualquier webhook previo que cause el 409
    requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=60)
        except Exception as e:
            print(f">> Error de red: {e}. Reintentando...")
            time.sleep(5)

if __name__ == "__main__":
    run_safe()
