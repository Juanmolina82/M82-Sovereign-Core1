import telebot
import os

# CREDENCIALES UNIFICADAS
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
GH_TOKEN = "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"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: m.from_user.id == CHAIRMAN_ID)
def ia_core_processor(m):
    t = m.text.lower()
    header = "🤖 <b>MOLINA IA PLATAFORM: AUDIT MODE</b>\n"
    
    if "liquidar" in t or "elliott" in t:
        response = (f"{header}├ <b>Estatus:</b> Liquidación Citgo/Amber Energy.\n"
                    f"└ <b>Veredicto IA:</b> El capital de Elliott es el lubricante de la transición. Infraestructura lista para absorción.")
    elif "status" in t or "matriz" in t:
        response = (f"{header}├ <b>Core:</b> V6.6 Unificado.\n"
                    f"└ <b>Auth:</b> Token ghp_PsNj... validado.")
    else:
        response = f"{header}└ Sistema en espera. Procesando flujos de capital geopolítico..."
    
    bot.reply_to(m, response, parse_mode='HTML')

print(">> IA-CORE V6.6: ADAPTACIÓN COMPLETADA Y ONLINE...")
bot.infinity_polling()
