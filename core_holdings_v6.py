import telebot
import time

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.from_user.id == CHAIRMAN_ID)
def response(m):
    t = m.text.lower()
    header = "🦅 <b>M82 HOLDINGS - SISTEMA RESTABLECIDO</b>\n"
    if "status" in t or "prueba" in t:
        msg = f"{header}├ <b>Estado:</b> ONLINE (Resucitado)\n└ <b>Veredicto:</b> Matriz activa y escuchando."
    else:
        msg = f"{header}└ <b>M82:</b> Core operativo. Procesando directivas de reconstrucción..."
    bot.reply_to(m, msg, parse_mode='HTML')

def run():
    print(">> RESUCITANDO MATRIZ M82...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=40)
        except Exception:
            time.sleep(5)

if __name__ == "__main__":
    run()
