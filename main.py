from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = ""

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Olá! Eu sou seu bot em Python."
    )

# Comando /ajuda
async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Comandos disponíveis:\n/start\n/ajuda"
    )

# Criar aplicação
app = ApplicationBuilder().token(TOKEN).build()

# Adicionar comandos
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ajuda", ajuda))

# Rodar bot
print("Bot rodando...")
app.run_polling()