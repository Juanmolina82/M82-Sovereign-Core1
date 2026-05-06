import telebot
import os
import time

# CONFIGURACIÓN FINAL ABSOLUTA
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

def motor_final(texto):
    t = texto.lower()
    header = "⚖️ <b>MOLINA GLOBAL: CORE V6.9 FINAL</b>\n"
    
    if "liquidar" in t or "elliott" in t:
        return (f"{header}├ <b>Protocolo:</b> Saneamiento por Liquidación.\n"
                f"├ <b>Estatus:</b> Elliott/Amber operando como motor de reset.\n"
                f"└ <b>Veredicto:</b> Transición de capital autorizada.")
    
    if "matriz" in t or "final" in t:
        return (f"{header}├ <b>Versión:</b> Unificación Final Sellada.\n"
                f"├ <b>Auth:</b> UNIFIED_KEY_FINAL Activa.\n"
                f"└ <b>Infraestructura:</b> Lista para reconstrucción 2026.")

    return f"{header}└ Sistema Blindado. Esperando órdenes del Chairman."

@bot.message_handler(func=lambda m: m.from_user.id == CHAIRMAN_ID)
def handle_final(m):
    bot.reply_to(m, motor_final(m.text), parse_mode='HTML')

if __name__ == "__main__":
    print(">> CORE V6.9 FINAL: MATRIZ SELLADA Y EN OPERACIÓN...")
    while True:
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception:
            time.sleep(5)
