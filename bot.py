from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# قائمة لتخزين الأرقام الوهمية
virtual_numbers = []

# دالة لمعالجة الأمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت الأرقام الوهمية. استخدم /addnumber لإضافة رقم.')

# دالة لمعالجة الأمر /addnumber
def add_number(update: Update, context: CallbackContext) -> None:
    number = ' '.join(context.args)  # الحصول على الرقم من الرسالة
    if number:
        virtual_numbers.append(number)  # إضافة الرقم إلى القائمة
        update.message.reply_text(f'تمت إضافة الرقم: {number}')
    else:
        update.message.reply_text('الرجاء إدخال رقم صحيح.')

# دالة لمعالجة الأمر /listnumbers
def list_numbers(update: Update, context: CallbackContext) -> None:
    if virtual_numbers:
        update.message.reply_text('الأرقام الوهمية:\n' + '\n'.join(virtual_numbers))
    else:
        update.message.reply_text('لا توجد أرقام مُضافة.')

# الدالة الرئيسية لتشغيل البوت
def main() -> None:
    # استبدل 'YOUR_TOKEN' برمز البوت الذي حصلت عليه
    updater = Updater("7564689893:AAFsGKrRAVSZteeUZ75JQVZlKY24BtSwUcw")

    # الحصول على dispatcher لتسجيل الأوامر
    dispatcher = updater.dispatcher

    # تسجيل الأوامر
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("addnumber", add_number))
    dispatcher.add_handler(CommandHandler("listnumbers", list_numbers))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()