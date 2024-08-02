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
            bot.send_message(message.chat.id, "برنامه‌سازی پیشرفته", reply_markup=lesson_btn)
            bot.register_next_step_handler(message, advance_programing_handler)

    elif message.text=="پایگاه داده":
        bot.send_message(message.chat.id, "پایگاه داده", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, dbms_handler)

    elif message.text=="پردازش تصاویررقومی":
        bot.send_message(message.chat.id, "پردازش تصاویررقومی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, image_procces_handler)

    elif message.text=="پویشگرهای لیزری":
        bot.send_message(message.chat.id, "پویشگرهای لیزری", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, laser_handler)

    elif message.text == "تئوری برآورد":
        bot.send_message(message.chat.id, "تئوری برآورد", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, teory_handler)

    elif message.text=="جبر خطی":
        bot.send_message(message.chat.id, "جبر خطی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, jabr_handler)

    elif message.text=="تحلیل اطلاعات مکانی":
        bot.send_message(message.chat.id, "تحلیل اطلاعات مکانی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, tahlil_handler)

    elif message.text=="روش‌های اجرای ساختمان":
        bot.send_message(message.chat.id, "روش‌های اجرای ساختمان", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, nader_handler)

    elif message.text=="حدنگاری":
        bot.send_message(message.chat.id, "حدنگاری", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, had_handler)

    elif message.text=="زیرسازی و روسازی":
        bot.send_message(message.chat.id,"زیرسازی و روسازی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, zirro_handler)

    elif message.text=="ریاضیات مهندسی":
        bot.send_message(message.chat.id, "ریاضیات مهندسی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, riazi_handler)

    elif message.text=="ژئودزی ماهواره‌ای":
        bot.send_message(message.chat.id, "ژئودزی ماهواره‌ای", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, gps_handler)

    elif message.text=="ژئودزی فیزیکال":
        bot.send_message(message.chat.id, "ژئودزی فیزیکال", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, fizical_handler)

    elif message.text=="سنجش از دور":
        bot.send_message(message.chat.id, "سنجش از دور", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, rs_handler)

    elif message.text=="ژئودزی هندسی":
        bot.send_message(message.chat.id, "ژئودزی هندسی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, hendesi_handler)

    elif message.text=="عملیات مبانی نقشه‌برداری":
        bot.send_message(message.chat.id, "عملیات مبانی نقشه‌برداری", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, amaliat_mabani_handler)

    elif message.text=="فتوگرامتری بردکوتاه":
        bot.send_message(message.chat.id, "فتوگرامتری بردکوتاه", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, kotah_handler)

    elif message.text=="فتوگرامتری تحلیلی":
        bot.send_message(message.chat.id, "فتوگرامتری تحلیلی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, tahlili_handler)

    elif message.text=="فیزیک نور":
        bot.send_message(message.chat.id, "فیزیک نور", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, fizik_handler)

    elif message.text=="کارتوگرافی":
        bot.send_message(message.chat.id, "کارتوگرافی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, carto_handler)

    elif message.text=="کاربردهای فتوگرامتری":
        bot.send_message(message.chat.id, "کاربردهای فتوگرامتری", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, karbord_handler)

    elif message.text=="کاربرد های GIS":
        bot.send_message(message.chat.id, "کاربرد های GIS", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, kargis_handler)

    elif message.text=="مبانی فتوگرامتری":
        bot.send_message(message.chat.id, "مبانی فتوگرامتری", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, mabaniphoto_handler)

    elif message.text=="مبانی نجوم و ژئودزی":
        bot.send_message(message.chat.id, "مبانی نجوم و ژئودزی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, mabani_geo_handler)

    elif message.text=="مبانی نقشه‌برداری":
        bot.send_message(message.chat.id, "مبانی نقشه‌برداری", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, mabani_naghse_handler)

    elif message.text== "نقشه برداری ثبتی":
        bot.send_message(message.chat.id, "نقشه برداری ثبتی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, sabti_handler)

    elif message.text=="مصالح ساختمانی":
        bot.send_message(message.chat.id, "مصالح ساختمانی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, masaleh_handler)

    elif message.text=="نقشه‌برداری مسیر و زیرزمینی":
        bot.send_message(message.chat.id, "نقشه‌برداری مسیر و زیرزمینی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, masir_handler)

    elif message.text == "نقشه‌برداری ژئودتیک":
        bot.send_message(message.chat.id, "نقشه‌برداری ژئودتیک", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, geodetic_handler)

    elif message.text=="هیدروگرافی":
        bot.send_message(message.chat.id, "هیدروگرافی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, hydro_handler)

    elif message.text=="هندسه دیفرانسیل":
        bot.send_message(message.chat.id, "هندسه دیفرانسیل", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, hendese_handler)

def urban_planning_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def advance_programing_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def dbms_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def image_procces_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def laser_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def teory_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def jabr_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def tahlil_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def nader_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def had_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def zirro_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def riazi_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def gps_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def fizical_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def rs_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def hendesi_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def amaliat_mabani_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def kotah_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def tahlili_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def fizik_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def carto_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def karbord_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def kargis_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def mabaniphoto_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def mabani_geo_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def mabani_naghse_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def sabti_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def masaleh_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def masir_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def geodetic_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def hydro_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def hendese_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)
bot.infinity_polling()