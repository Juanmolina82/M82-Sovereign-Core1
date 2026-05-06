import telebot
import time

# CONFIGURACIÓN UNIFICADA DE PRUEBA
TOKEN = "8600412468:AAE9rQQC2Z0ReE4qJ1R9amDfm5m4sO2-wM4"
CHAIRMAN_ID = 1020305418
bot = telebot.TeleBot(TOKEN)

def generar_veredicto(comando):
    c = comando.lower()
    header = "🏛️ <b>REPORTE DE INTEGRIDAD MOLINA GLOBAL</b>\n"
    
    if "prueba" in c:
        return (f"{header}├ <b>Estatus:</b> ONLINE\n"
                f"├ <b>Matriz:</b> V6.9.1 (Sellada)\n"
                f"└ <b>Veredicto:</b> Conexión exitosa. El Chairman tiene el control.")
    
    if "elliott" in c or "liquidar" in c:
        return (f"{header}├ <b>Módulo:</b> Auditoría de Capital\n"
                f"├ <b>Objetivo:</b> Liquidación de pasivos Citgo.\n"
                f"└ <b>Intel:</b> Transición operativa tras saneamiento de Amber Energy.")

    return f"{header}└ <i>Esperando instrucciones tácticas...</i>"

@bot.message_handler(func=lambda m: m.from_user.id == CHAIRMAN_ID)
def handle_test(m):
    print(f">> Comando recibido: {m.text}")
    bot.reply_to(m, generar_veredicto(m.text), parse_mode='HTML')

if __name__ == "__main__":
    print(">> BOT EN LÍNEA. ESCRIBE 'PRUEBA' EN TELEGRAM...")
    bot.infinity_polling()
