import telebot
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup

bot_hash = "6303262445:AAENdfZTD3Jp5tRIcxOapiVAAUqiqSk23aw"
bot=telebot.TeleBot(bot_hash)

keybord_markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
keybord_markup.add("برنامه‌ریزی شهری", "برنامه‌سازی پیشرفته", "پایگاه داده", "پردازش تصاویررقومی", "تئوری برآورد",
               "پویشگرهای لیزری", "جبر خطی", "تحلیل اطلاعات مکانی", "روش‌های اجرای ساختمان", "حدنگاری", "زیرسازی و روسازی",
               "ریاضیات مهندسی", "ژئودزی ماهواره‌ای", "ژئودزی فیزیکال", "سنجش از دور", "ژئودزی هندسی",
               "عملیات مبانی نقشه‌برداری", "سیستم اطلاعات مکانی", "فتوگرامتری بردکوتاه", "فتوگرامتری تحلیلی",
               "فیزیک نور", "کارتوگرافی", "کاربردهای فتوگرامتری", "کاربرد های GIS", "مبانی فتوگرامتری",
               "مبانی نجوم و ژئودزی", "مبانی نقشه‌برداری", "نقشه برداری ثبتی", "مصالح ساختمانی",
               "نقشه‌برداری مسیر و زیرزمینی", "نقشه‌برداری ژئودتیک", "هیدروگرافی", "هندسه دیفرانسیل")

def join_channel_button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("عضویت", url="https://t.me/geomatic_nit"))
    markup.add(InlineKeyboardButton("عضو شدم✅", callback_data="check_join"))
    return markup

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join_callback(call):
    user_id = call.from_user.id
    channel_id = "@geomatic_nit"
    member = bot.get_chat_member(channel_id, user_id)
    if member.status == "member":
        send_welcome(call.message)
    else:
        bot.answer_callback_query(call.id, "🙂برای استفاده از ربات باید توی کانال انجمن عضو بشید:", show_alert=True)

channels = ["@geomatic_nit"]
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    for channel in channels:
        member = bot.get_chat_member(channel, user_id)
        if member.status not in ["kicked", "left"]:
            bot.send_message(message.chat.id, "چه کمکی می‌توانم به شما کنم؟", reply_markup=keyboard_markup)
            return
    bot.send_message(message.chat.id, "🙂برای استفاده از ربات حتما باید توی کانال های زیر عضو بشین:", reply_markup=join_channel_button())

bot.infinity_polling()