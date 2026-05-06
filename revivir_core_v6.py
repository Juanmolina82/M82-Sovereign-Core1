import telebot
import os

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
bot = telebot.TeleBot(TOKEN)

# Verificación de Arquitectura
carpetas = ["AUDITORIA_ELLIOTT", "MOLINA_IA_PLATAFORM"]
integracion = {c: os.path.exists(c) for c in carpetas}

@bot.message_handler(commands=['start', 'status'])
def send_status(m):
    resumen = "\n".join([f"📁 {k}: {'✅ OK' if v else '❌ MISSING'}" for k, v in integracion.items()])
    bot.reply_to(m, f"🏛️ <b>CORE V6 - REPORTE DE ARQUITECTURA</b>\n\n{resumen}\n\n🦅 <b>M82:</b> Sistema listo.", parse_mode='HTML')

print(">> COMPROBANDO ARQUITECTURA...")
bot.infinity_polling()
