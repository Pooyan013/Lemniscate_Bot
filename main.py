import telebot
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup

bot_hash = "6303262445:AAENdfZTD3Jp5tRIcxOapiVAAUqiqSk23aw"
bot=telebot.TeleBot(bot_hash)
lesson_name= ["برنامه‌ریزی شهری", "برنامه‌سازی پیشرفته", "پایگاه داده", "پردازش تصاویررقومی", "تئوری برآورد",
               "پویشگرهای لیزری", "جبر خطی", "تحلیل اطلاعات مکانی", "روش‌های اجرای ساختمان", "حدنگاری", "زیرسازی و روسازی",
               "ریاضیات مهندسی", "ژئودزی ماهواره‌ای", "ژئودزی فیزیکال", "سنجش از دور", "ژئودزی هندسی",
               "عملیات مبانی نقشه‌برداری", "سیستم اطلاعات مکانی", "فتوگرامتری بردکوتاه", "فتوگرامتری تحلیلی",
               "فیزیک نور", "کارتوگرافی", "کاربردهای فتوگرامتری", "کاربرد های GIS", "مبانی فتوگرامتری",
               "مبانی نجوم و ژئودزی", "مبانی نقشه‌برداری", "نقشه برداری ثبتی", "مصالح ساختمانی",
               "نقشه‌برداری مسیر و زیرزمینی", "نقشه‌برداری ژئودتیک", "هیدروگرافی", "هندسه دیفرانسیل"]

keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
keyboard_markup.add("برنامه‌ریزی شهری", "برنامه‌سازی پیشرفته", "پایگاه داده", "پردازش تصاویررقومی", "تئوری برآورد",
               "پویشگرهای لیزری", "جبر خطی", "تحلیل اطلاعات مکانی", "روش‌های اجرای ساختمان", "حدنگاری", "زیرسازی و روسازی",
               "ریاضیات مهندسی", "ژئودزی ماهواره‌ای", "ژئودزی فیزیکال", "سنجش از دور", "ژئودزی هندسی",
               "عملیات مبانی نقشه‌برداری", "سیستم اطلاعات مکانی", "فتوگرامتری بردکوتاه", "فتوگرامتری تحلیلی",
               "فیزیک نور", "کارتوگرافی", "کاربردهای فتوگرامتری", "کاربرد های GIS", "مبانی فتوگرامتری",
               "مبانی نجوم و ژئودزی", "مبانی نقشه‌برداری", "نقشه برداری ثبتی", "مصالح ساختمانی",
               "نقشه‌برداری مسیر و زیرزمینی", "نقشه‌برداری ژئودتیک", "هیدروگرافی", "هندسه دیفرانسیل")

lesson_btn = ReplyKeyboardMarkup(resize_keyboard=True ,row_width=2)
lesson_btn.add("🔙","جزوه", "نمونه سوال" , "ویدئو")

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
            bot.send_message(message.chat.id, "تو کدوم درس نیاز به کمک داری؟", reply_markup=keyboard_markup)
            return
    bot.send_message(message.chat.id, "🙂برای استفاده از ربات حتما باید توی کانال های زیر عضو بشین:", reply_markup=join_channel_button())

@bot.message_handler()
def main(message):
    channel1=-1002031480440
    bot.send_chat_action(message.chat.id,action="typing")
    if message.text == "🔙":
        bot.send_message(message.chat.id,"بازگشت" ,reply_markup=keyboard_markup)
    elif message.text=="برنامه‌ریزی شهری": 
          bot.send_message(message.chat.id, "برنامه‌ریزی شهری", reply_markup=lesson_btn)
          bot.register_next_step_handler(message, urban_planning_handler)
          
    elif message.text=="برنامه‌سازی پیشرفته":
            Ap=[38,39,40,41,42,43,44,45,46,47,48]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[38,39,40,41,42,43,44,45,46,47,48])
    elif message.text=="پایگاه داده":
            Payagh=[61,62,63,64,65,66]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[61,62,63,64,65,66])
    elif message.text=="پردازش تصاویررقومی":
            DIP=[49,50,51,52,53,54,55,56,57,58,59]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[49,50,51,52,53,54,55,56,57,58,59])
    elif message.text=="پویشگرهای لیزری":
           bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[68,69,515])
    elif message.text == "تئوری برآورد":
           Teory=[73,74,75,76,77,78]
           bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[73,74,75,76,77,78,497,498,499,520])
    elif message.text=="جبر خطی":
        Jabr=[90,91,92,93,94,95,96,97,98,99]
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[90,91,92,93,94,95,96,97,98,99,488])
    elif message.text=="تحلیل اطلاعات مکانی":
           Tahlil=[80,81,82,83,84,85]
           bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[80,81,82,83,84,85])
    elif message.text=="روش‌های اجرای ساختمان":
        Ejra=[300,301,302,303,304,305,306,307,308,309]
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[300,301,302,303,304,305,306,307,308,309])
    elif message.text=="حدنگاری":
        bot.send_message(message.chat.id,"متاسفاته برای این درس هنوز جزوه ای نداریم😑",reply_markup=lesson_btn)
    elif message.text=="زیرسازی و روسازی":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[87,512,521])
    elif message.text=="ریاضیات مهندسی":
            riazi=[287,288,289,290,291,292,293,294]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[287,288,289,290,291,292,293,294])
    elif message.text=="ژئودزی ماهواره‌ای":
            Gps=[111,112,113,114,115,116,117,118,119,120,121]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[111,112,113,114,115,116,117,118,119,120,121])
    elif message.text=="ژئودزی فیزیکال":
            phyz=[101,102,103,104]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[101,102,103,104])
    elif message.text=="سنجش از دور":
           Rs=[123,124,125,126,127,128,129,130,131,132,133]
           bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[123,124,125,126,127,128,129,130,131,132,133])
    elif message.text=="ژئودزی هندسی":
            hendesi=[106,107,108,109]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[106,107,108,109,495])
    elif message.text=="عملیات مبانی نقشه‌برداری":
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[311,312])
    elif message.text=="سیستم اطلاعات مکانی":
            Gis=[135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,496,518])
    elif message.text=="فتوگرامتری بردکوتاه":
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[298])
    elif message.text=="فتوگرامتری تحلیلی":
            PhTahlili=[241,242,243,244,245,246,247,248,249,250]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[241,242,243,244,245,246,247,248,249,250,493,519])
    elif message.text=="فیزیک نور":
           bot.send_message(message.chat.id,"متاسفاته برای این درس هنوز جزوه ای نداریم😑",reply_markup=lesson_btn)
    elif message.text=="کارتوگرافی":
            Carto=[216,217,218,219,220,221,222,223,224,225]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[216,217,218,219,220,221,222,223,224,225])
    elif message.text=="کاربردهای فتوگرامتری":
            karbord=[201,202,203,204,205,206,207,208,209,210,211,212]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[201,202,203,204,205,206,207,208,209,210,211,212])
    elif message.text=="کاربرد های GIS":
            KarbordGIS=[179,180,181,182,183,184,185,186,187]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[179,180,181,182,183,184,185,186,187])
    elif message.text=="مبانی فتوگرامتری":
            Mphoto=[262,263,264,265,266,267,268,269,270,271,272,273,274,275]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[262,263,264,265,266,267,268,269,270,271,272,273,274,275])
    elif message.text=="مبانی نجوم و ژئودزی":
            MGeo=[252,253,254,255,256,257,258,259,260]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[252,253,254,255,256,257,258,259,260,494,513,514])
    elif message.text=="مبانی نقشه‌برداری":
            MNaghshe=[228,229,230,231,232,233,234,235,236,237,238]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[228,229,230,231,232,233,234,235,236,237,238,502])
    elif message.text== "نقشه برداری ثبتی":
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[296,490])
    elif message.text=="مصالح ساختمانی":
            bot.send_message(message.chat.id,"متاسفاته برای این درس هنوز جزوه ای نداریم😑",reply_markup=lesson_btn)
    elif message.text=="نقشه‌برداری مسیر و زیرزمینی":
            naghshe=[277,278,279,280,281,282,283,284,285]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[277,278,279,280,281,282,283,284,285,470,500])
    elif message.text == "نقشه‌برداری ژئودتیک":
            Geodetic=[154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177]
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,487,491])
    elif message.text=="هیدروگرافی":
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[2,3])
    elif message.text=="هندسه دیفرانسیل":
            bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[190,191,192,193,194,195,196,197,198,199,486,516,517])

def urban_planning_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)
    else:
        bot.send_message(message.chat.id, "لطفاً یکی از گزینه‌های موجود را انتخاب کنید.", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, urban_planning_handler)

bot.infinity_polling()