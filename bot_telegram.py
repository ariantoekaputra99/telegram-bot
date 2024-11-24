from telegram import Update, ChatPermissions
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram import filters

# Masukkan token bot Anda di sini
TOKEN = "7811119595:AAETqRxt0Nfz7uNDQffHFjJ3bTrXyFo-aiA"

# Fungsi untuk menyambut anggota baru
def welcome(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        welcome_message = f"Selamat datang, {member.full_name}! Jangan lupa baca rules di deskripsi 😊"
        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

# Fungsi untuk menghapus pesan spam atau link
def filter_messages(update: Update, context: CallbackContext):
    message = update.message

    # Periksa apakah pengirim pesan adalah admin
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Dapatkan daftar admin
    admins = context.bot.get_chat_administrators(chat_id)
    admin_ids = [admin.user.id for admin in admins]

    if user_id in admin_ids:
        # Jika pengirim adalah admin, abaikan pesan
        return

    # Hapus pesan yang mengandung link atau mention bot
    if "http" in message.text or "@" in message.text:
        message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Pesan dengan link atau mention bot dihapus!")

# Fungsi untuk memulai bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Halo! Saya siap membantu. 😊")

# Fungsi utama untuk menjalankan bot
def main():
    # Menggunakan Application dari telegram.ext pada versi terbaru (v20+)
    from telegram.ext import Application

    # Membuat aplikasi dengan token
    application = Application.builder().token(TOKEN).build()

    # Handler untuk menyambut anggota baru
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    
    # Handler untuk memfilter pesan
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_messages))
    
    # Handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    # Mulai bot
    application.run_polling()

if __name__ == "__main__":
    main()
