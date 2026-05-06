import telebot
import datetime
import time
import os

# CONFIGURACIÓN UNIFICADA
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

def motor_unificado(texto):
    t = texto.lower()
    # Módulo de Transición y Elliott
    if "liquidar" in t or "elliott" in t:
        return (f"⚡ <b>MATRIZ V6.1: ESTRATEGIA DE TRANSICIÓN</b>\n"
                f"├ <b>Veredicto:</b> Liquidación por Elliott Management aprobada.\n"
                f"└ <b>Objetivo:</b> Reset de infraestructura para entrada masiva de capital.")
    
    # Módulo de Geopolítica (Project Freedom)
    if "freedom" in t or "ormuz" in t or "trump" in t:
        return (f"🚢 <b>INTEL: PROJECT FREEDOM & STRATEGY</b>\n"
                f"├ <b>Estatus:</b> Apertura forzada del Estrecho de Hormuz.\n"
                f"└ <b>Impacto Citgo:</b> Revalorización inmediata de activos logísticos.")

    # Módulo de Identidad Venezolana
    if "venezuela" in t or "libertad" in t:
        return (f"🇻🇪 <b>MOLINA GLOBAL: SOBERANÍA</b>\n"
                f"└ <b>Visión:</b> La reconstrucción nacional se financia con la eficiencia privada.")

    return "🏛️ <b>M82 UNIFIED CORE:</b> Nodo central operativo. Esperando parámetros de la Matriz..."

@bot.message_handler(func=lambda m: m.from_user.id == CHAIRMAN_ID)
def handle_all(m):
    print(f"[{datetime.datetime.now()}] Comando recibido: {m.text}")
    bot.reply_to(m, motor_unificado(m.text), parse_mode='HTML')

if __name__ == "__main__":
    print(">> MATRIZ UNIFICADA V6.1 LANZADA...")
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            time.sleep(5)
