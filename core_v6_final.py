import telebot
import os
import datetime

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

def get_status_report():
    modulos = {
        "🚛 LOGÍSTICA": "LOGISTICA_TRANSITO",
        "⚡ ENERGÍA": "ENERGIA_SOBERANA",
        "📈 EQUITIES": "EQUITIES_GLOBAL",
        "🦅 ELLIOTT/AMBER": "AUDITORIA_ELLIOTT"
    }
    reporte = "🏛️ <b>M82 HOLDINGS - REPORTE DE ACTIVOS</b>\n\n"
    for nombre, ruta in modulos.items():
        status = "✅" if os.path.exists(ruta) else "❌"
        reporte += f"{status} {nombre}\n"
    return reporte

@bot.message_handler(commands=['start', 'status', 'assets'])
def send_welcome(m):
    if m.from_user.id == CHAIRMAN_ID:
        reporte = get_status_report()
        reporte += f"\n📅 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        reporte += "\n\n🦅 <b>AGI M82:</b> Sistema alineado con Hedge Funds."
        bot.reply_to(m, reporte, parse_mode='HTML')

@bot.message_handler(func=lambda m: "milken" in m.text.lower() or "bloomberg" in m.text.lower())
def intel_report(m):
    msg = "🛰️ <b>M82 INTEL ADVISORY</b>\n\n"
    msg += "Analizando correlación entre Blackstone/KKR y activos de infraestructura local.\n"
    msg += "└ <i>Estatus:</i> Sincronizando con el Cobre (GitHub)."
    bot.reply_to(m, msg, parse_mode='HTML')

if __name__ == "__main__":
    print(">> BOT M82 AGI: OPERATIVO Y ENVIANDO...")
    bot.infinity_polling()
