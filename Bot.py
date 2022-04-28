from copyreg import dispatch_table
from telegram.ext import *
import BSCScan
import Constants as keys

def start_command(update, context):
    update.message.reply_text("Komut listesini görmek için /yardim komutunu kullanın")

def help_command(update, context):
    update.message.reply_text("""/yardim => Bu mesaj
/kaynak => Kaynak kodlarını gör
/sonBlock => Zincirdeki son bloğun ID'si
/islemBilgisi (hashKod) => Hash Kodu girilen işlemin bilgileri
/islemSayisi (blokId) => ID'si verilen bloğun içerdiği işlem sayısı
/tps (süre) => Verilen sürede gerçekleşen işlem sayısı                           
""")

def sourceCode_command(update, context):
    update.message.reply_text("github")

def latestBlock_command(update,context):
    update.message.reply_text(BSCScan.getLatestBlock())

def transactionInfo_command(update, context):
    update.message.reply_text(BSCScan.getTransactionInfo(context.args[0]))
    
def transactionCount_command(update, context):
    update.message.reply_text(BSCScan.getTransactionCount(int(context.args[0])))
    
def transactionInInterval_commdand(update, context):
    update.message.reply_text(BSCScan.transactionInInterval(int(context.args[0])))


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    disp = updater.dispatcher
    
    disp.add_handler(CommandHandler("basla", start_command))
    disp.add_handler(CommandHandler("yardim", help_command))
    disp.add_handler(CommandHandler("kaynak", sourceCode_command))
    disp.add_handler(CommandHandler("sonBlok", latestBlock_command))
    disp.add_handler(CommandHandler("islemBilgisi", transactionInfo_command))
    disp.add_handler(CommandHandler("islemSayisi", transactionCount_command))
    disp.add_handler(CommandHandler("tps", transactionInInterval_commdand))
    
    updater.start_polling()
    updater.idle()
    
      
main()    