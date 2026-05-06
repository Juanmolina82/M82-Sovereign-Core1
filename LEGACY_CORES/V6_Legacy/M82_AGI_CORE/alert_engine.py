import telebot
import datetime
import sys

TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

def enviar_veredicto_profundo(sector, detalle, metrics):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = (f"🦅 <b>M82 AGI - DEEP VERDICT</b>\n"
           f"━━━━━━━━━━━━━━━━━━━━\n"
           f"<b>Sector:</b> {sector}\n"
           f"<b>Análisis:</b> {detalle}\n\n"
           f"📊 <b>MÉTRICAS DE MERCADO:</b>\n{metrics}\n"
           f"━━━━━━━━━━━━━━━━━━━━\n"
           f"📌 <b>ESTATUS:</b> Sincronizado en Cobre ✅\n"
           f"📅 {fecha}")
    bot.send_message(CHAIRMAN_ID, msg, parse_mode='HTML')

if __name__ == "__main__":
    # Si se ejecuta con argumentos, los envía. Si no, envía el reporte de Milken completo.
    sector = "INFRAESTRUCTURA & EQUITIES"
    analisis = "Detección de acumulación institucional en PAVE e IGF ($10B+ AUM)."
    metrics = ("• PAVE: $56.19 (Descuento 0.8% vs NAV)\n"
               "• IGF: $67.55 (73% Institucional)\n"
               "• FANG: Giro a crecimiento de producción (3%)")
    enviar_veredicto_profundo(sector, analisis, metrics)
