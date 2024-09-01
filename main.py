import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

bot_hash = "6303262445:AAENdfZTD3Jp5tRIcxOapiVAAUqiqSk23aw"
bot = telebot.TeleBot(bot_hash)
lesson_name = [
    "برنامه‌ریزی شهری", "برنامه‌سازی پیشرفته", "پایگاه داده", "پردازش تصاویررقومی", "تئوری برآورد",
    "پویشگرهای لیزری", "جبر خطی", "تحلیل اطلاعات مکانی", "روش‌های اجرای ساختمان", "حدنگاری", "زیرسازی و روسازی",
    "ریاضیات مهندسی", "ژئودزی ماهواره‌ای", "ژئودزی فیزیکال", "سنجش از دور", "ژئودزی هندسی",
    "عملیات مبانی نقشه‌برداری", "سیستم اطلاعات مکانی", "فتوگرامتری بردکوتاه", "فتوگرامتری تحلیلی",
    "فیزیک نور", "کارتوگرافی", "کاربردهای فتوگرامتری", "کاربرد های GIS", "مبانی فتوگرامتری",
    "مبانی نجوم و ژئودزی", "مبانی نقشه‌برداری", "نقشه برداری ثبتی", "مصالح ساختمانی",
    "نقشه‌برداری مسیر و زیرزمینی", "نقشه‌برداری ژئودتیک", "هیدروگرافی", "هندسه دیفرانسیل"
]

keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
keyboard_markup.add(*lesson_name)

lesson_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
lesson_btn.add("جزوه", "نمونه سوال", "ویدئو", "🔙")

channels = ["@geomatic_nit"]
user_ids_file = "user_ids.txt"

def save_user_id(user_id):
    """ Save user_id to file if not already present """
    with open(user_ids_file, "a+") as file:
        file.seek(0)
        ids = file.read().splitlines()
        if str(user_id) not in ids:
            file.write(f"{user_id}\n")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    save_user_id(user_id)  
    for channel in channels:
        member = bot.get_chat_member(channel, user_id)
        if member.status not in ["kicked", "left"]:
            bot.send_message(message.chat.id, "تو کدوم درس نیاز به کمک داری؟", reply_markup=keyboard_markup)
            return
    bot.send_message(message.chat.id, "🙂برای استفاده از ربات حتما باید توی کانال های زیر عضو بشین:", reply_markup=join_channel_button())

@bot.message_handler(commands=["broadcast"])
def broadcast(message):
    if message.chat.type == "private" and message.from_user.id == ADMIN_USER_ID:
        broadcast_message = message.text.replace('/broadcast', '').strip()
        if broadcast_message:
            with open(user_ids_file, "r") as file:
                user_ids = file.readlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id.strip(), broadcast_message)
                    except Exception as e:
                        print(f"Failed to send message to {user_id}: {e}")
        else:
            bot.send_message(message.chat.id, "Please provide a message to broadcast.")

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

    elif message.text=="سیستم اطلاعات مکانی":
        bot.send_message(message.chat.id, "سیستم اطلاعات مکانی", reply_markup=lesson_btn)
        bot.register_next_step_handler(message, gis_handler)

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
    
    elif message.text == "عملیات GIS":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[438,439,440,441,442,443,444,445,446,447,448])
    elif message.text == "عملیات سنجش از دور":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[457,458,459,460,461,462,463,464,465,466])
    elif message.text == "عملیات کابردهای فتوگرامتری":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[450,451,452,453,454,455,456])
    elif message.text == "عملیات تحلیل های مکانی":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[468])
    elif message.text == "عملیات مبانی فتوگرامتری":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
def urban_planning_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[325])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

channel1=-1002031480440
def advance_programing_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[38,39,40,41,42,43,44,45,46,47,48])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[313])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def dbms_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[61,62,63,64,65,66])
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def image_procces_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[49,50,51,52,53,54,55,56,57,58,59])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[316,315,433,434,435,436,437])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def laser_handler(message):
    if message.text == "جزوه":
       bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[68,69,515])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[322])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def teory_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[73,74,75,76,77,78,497,498,499,520])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[396,397,398,399,400,401,402,403])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def jabr_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[90,91,92,93,94,95,96,97,98,99,488])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[373])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def tahlil_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[80,81,82,83,84,85])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[405,406,407])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def nader_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[300,301,302,303,304,305,306,307,308,309])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[327,328,329,330,331,332])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def had_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id,"متاسفاته برای این درس هنوز جزوه ای نداریم😑",reply_markup=lesson_btn)
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[421])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def zirro_handler(message):
    if message.text == "جزوه":
       bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[87,512,521])
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def riazi_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[287,288,289,290,291,292,293,294])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[385,386,387,388,389])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def gps_handler(message):
    if message.text == "جزوه":
         bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[111,112,113,114,115,116,117,118,119,120,121])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[355])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def fizical_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[101,102,103,104])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[334,335,336,337,338,339,340])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def rs_handler(message):
    if message.text == "جزوه":
       bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[123,124,125,126,127,128,129,130,131,132,133])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[391,392,393,394])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def hendesi_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[106,107,108,109,495])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[360,361,362,363])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def amaliat_mabani_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[311,312])
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def gis_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,496,518])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[351,352,353])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def kotah_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[298])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[419])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def tahlili_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[241,242,243,244,245,246,247,248,249,250,493,519])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[409,410,411,412,413])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def fizik_handler(message):
    if message.text == "جزوه":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز جزوه ای نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[342,343])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def carto_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[216,217,218,219,220,221,222,223,224,225])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[423,489,])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def karbord_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[201,202,203,204,205,206,207,208,209,210,211,212])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[425])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def kargis_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[179,180,181,182,183,184,185,186,187])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[367,368])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def mabaniphoto_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[262,263,264,265,266,267,268,269,270,271,272,273,274,275])
    elif message.text == "نمونه سوال":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز نمونه سوالی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def mabani_geo_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[252,253,254,255,256,257,258,259,260,494,513,514])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[370,371])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def mabani_naghse_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[228,229,230,231,232,233,234,235,236,237,238,502])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[376,377,378,379,380])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def sabti_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[296,490])
    elif message.text == "نمونه سوال":
       bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[416,417])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def masaleh_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[277,278,279,280,281,282,283,284,285,470,500])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[427])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def masir_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[277,278,279,280,281,282,283,284,285,470,500])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[381,382,383])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def geodetic_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,487,491])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[345,346,347,348,349])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def hydro_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[2,3])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[365])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)

def hendese_handler(message):
    if message.text == "جزوه":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[190,191,192,193,194,195,196,197,198,199,486,516,517])
    elif message.text == "نمونه سوال":
        bot.copy_messages(chat_id=message.chat.id,from_chat_id=channel1,message_ids=[358,359])
    elif message.text == "ویدئو":
        bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)
    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت", reply_markup=keyboard_markup)
bot.infinity_polling()