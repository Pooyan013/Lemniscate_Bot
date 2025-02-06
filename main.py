import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from keys import *

import sqlite3
from datetime import datetime

bot = telebot.TeleBot(hash)
lesson_name = [
    "برنامه‌ریزی شهری", "برنامه‌سازی پیشرفته", "پایگاه داده", "پردازش تصاویررقومی", "تئوری برآورد",
    "پویشگرهای لیزری", "جبر خطی", "تحلیل اطلاعات مکانی", "روش‌های اجرای ساختمان", "حدنگاری", "زیرسازی و روسازی",
    "ریاضیات مهندسی", "ژئودزی ماهواره‌ای", "ژئودزی فیزیکال", "سنجش از دور", "ژئودزی هندسی",
    "عملیات مبانی نقشه‌برداری", "سیستم اطلاعات مکانی", "فتوگرامتری بردکوتاه", "فتوگرامتری تحلیلی",
    "فیزیک نور", "کارتوگرافی", "کاربردهای فتوگرامتری", "کاربرد های GIS", "مبانی فتوگرامتری",
    "مبانی نجوم و ژئودزی", "مبانی نقشه‌برداری", "نقشه برداری ثبتی", "مصالح ساختمانی",
    "نقشه‌برداری مسیر و زیرزمینی", "نقشه‌برداری ژئودتیک", "هیدروگرافی", "هندسه دیفرانسیل",
    "مدیریت پروژه",
]

keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
keyboard_markup.add(*lesson_name)

lesson_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
lesson_btn.add("جزوه📕", "نمونه سوال📑", "ویدئو🎞", "🔙")

channels = ["@geomatic_nit"]
user_ids_file = "user_ids.txt"

#_______________________SaveUserId________________________________
def save_user_id(user_id):
    with open(user_ids_file, "a+") as file:
        file.seek(0)
        ids = file.read().splitlines()
        if str(user_id) not in ids:
            file.write(f"{user_id}\n")

def join_channel_button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("عضویت", url="https://t.me/geomatic_nit"))
    markup.add(InlineKeyboardButton("عضو شدم✅", callback_data="check_join"))
    return markup

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.first_name  
    save_user_id(user_id)

    update_user_data(user_id, username) 
    for channel in channels:
        member = bot.get_chat_member(channel, user_id)
        if member.status not in ["kicked", "left"]:
            bot.send_message(message.chat.id, f"سلام {username}! تو کدوم درس نیاز به کمک داری؟", reply_markup=keyboard_markup)
            return

    bot.send_message(message.chat.id, f"سلام {username}! 🙂برای استفاده از ربات حتما باید توی کانال‌های زیر عضو بشی:", reply_markup=join_channel_button())

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_join_callback(call):
    user_id = call.from_user.id
    channel_id = "@geomatic_nit"
    member = bot.get_chat_member(channel_id, user_id)
    if member.status == "member":
        send_welcome(call.message)
    else:
        bot.answer_callback_query(call.id, "🙂برای استفاده از ربات باید توی کانال انجمن عضو بشید:", show_alert=True)

#_______________________________CreateUserDatabase_________________________________

def create_users_table():
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            username TEXT,
            usage_count INTEGER DEFAULT 0,
            last_used TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_users_table()
def update_user_data(user_id, username):
    
    conn = sqlite3.connect('Users.db', check_same_thread=False)
    cursor = conn.cursor()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        cursor.execute("""
            UPDATE users
            SET usage_count = usage_count + 1, last_used = ?
            WHERE user_id = ?
        """, (now, user_id))
    else:
        cursor.execute("""
            INSERT INTO users (user_id, username, usage_count, last_used)
            VALUES (?, ?, 1, ?)
        """, (user_id, username, now))

    conn.commit()
    conn.close()

user_lessons = {}  
channel1 = -1002031480440

#_____________________________Broadcast______________________________
@bot.message_handler(commands=["broadcast"])
def broadcast(message):
    if message.chat.type == "private" and message.from_user.id == 101108999:
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

#__________________________________Sender_______________________________
@bot.message_handler()
def main(message):
    if message.text in lesson_name:
        user_lessons[message.chat.id] = message.text  
        bot.send_message(message.chat.id, "به کدومشون احتیاج داری؟", reply_markup=lesson_btn)

    elif message.text == "جزوه📕":
        lesson = user_lessons.get(message.chat.id)
        if lesson and lesson in handout:
            bot.copy_messages(chat_id=message.chat.id, from_chat_id=channel1, message_ids=handout[lesson])
            bot.send_message(message.chat.id, "مشکلی وجود داره یا فایلی داری که تو ربات نیست حتما برام بفرستش ✌️\n @Pooyan013", reply_markup=keyboard_markup)
        else:
            bot.send_message(message.chat.id, "متاسفانه برای این درس جزوه‌ای موجود نیست😑", reply_markup=keyboard_markup)

    elif message.text == "نمونه سوال📑":
        lesson = user_lessons.get(message.chat.id)
        if lesson and lesson in exams:
            bot.copy_messages(chat_id=message.chat.id, from_chat_id=channel1, message_ids=exams[lesson])
            bot.send_message(message.chat.id, "مشکلی وجود داره یا فایلی داری که تو ربات نیست حتما برام بفرستش ✌️\n @Pooyan013", reply_markup=keyboard_markup)
        else:
            bot.send_message(message.chat.id, "متاسفانه برای این درس نمونه سوالی موجود نیست😑", reply_markup=keyboard_markup)

    elif message.text == "ویدئو🎞":
        lesson = user_lessons.get(message.chat.id)
        if lesson == "تحلیل اطلاعات مکانی":
            bot.copy_messages(chat_id=message.chat.id, from_chat_id=channel1, message_ids=[468])
        elif lesson == "سیستم اطلاعات مکانی":
            bot.copy_messages(chat_id=message.chat.id, from_chat_id=channel1, message_ids=[438, 439, 440, 441])
        elif lesson == "سنجش از دور":
            bot.copy_messages(chat_id=message.chat.id, from_chat_id=channel1, message_ids=[457, 458, 459, 460, 461, 462, 463, 464, 465, 466])
        elif lesson == "کاربردهای فتوگرامتری":
            bot.copy_messages(chat_id=message.chat.id, from_chat_id=channel1, message_ids=[450, 451, 452, 453, 454, 455, 456])
        else:
            bot.send_message(message.chat.id, "متاسفانه برای این درس هنوز ویدئویی نداریم😑", reply_markup=keyboard_markup)

    elif message.text == "🔙":
        bot.send_message(message.chat.id, "بازگشت به منوی اصلی", reply_markup=keyboard_markup)

bot.infinity_polling()
