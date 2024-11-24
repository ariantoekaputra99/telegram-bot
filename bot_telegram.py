from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Token bot yang didapatkan dari BotFather
TOKEN = '1589813736:AAHcBLf-nsqUDDBoqhI3VUCp_XglDZGJDrc'

# Fungsi untuk menyambut anggota baru
def welcome(update: Update, context: CallbackContext) -> None:
    for member in update.message.new_chat_members:
        update.message.reply_text(f"Selamat datang, {member.full_name}!, Jangan Lupa baca rules di deskripsi ya 🎉")

# Fungsi untuk menghapus pesan yang berisi link
def remove_links(update: Update, context: CallbackContext) -> None:
    if any(word in update.message.text for word in ["http://", "https://", ".com", ".id", ".net", ".org"]):
        update.message.delete()

# Fungsi utama untuk menjalankan bot
def main() -> None:
    # Membuat Updater dan menyambungkan dengan token API
    updater = Updater(TOKEN)

    # Mendapatkan dispatcher untuk menambahkan handler
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk menyambut anggota baru
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # Menambahkan handler untuk mendeteksi dan menghapus pesan berisi link
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, remove_links))

    # Mulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
