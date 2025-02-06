# ربات انجمن علمی نقشه‌برداری دانشگاه نوشیروانی



ربات تلگرامی انجمن علمی نقشه‌برداری دانشگاه نوشیروانی، یک ابزار مفید برای دانشجویان رشته نقشه‌برداری است که به آن‌ها کمک می‌کند تا به راحتی به منابع درسی، جزوات، نمونه سوالات و ویدئوهای آموزشی دسترسی داشته باشند.

---

## 🎯 هدف ربات

این ربات با هدف تسهیل دسترسی دانشجویان به منابع آموزشی و اطلاع‌رسانی‌های انجمن علمی نقشه‌برداری دانشگاه نوشیروانی طراحی شده است. دانشجویان می‌توانند از طریق این ربات به موارد زیر دسترسی داشته باشند:

- 📕 **جزوات درسی**
- 📑 **نمونه سوالات امتحانی**
- 🎞 **ویدئوهای آموزشی**
- 🔔 **اطلاعیه‌های انجمن علمی**

---

## 🛠️ امکانات ربات

- **دسترسی به منابع درسی:** دانشجویان می‌توانند جزوات و نمونه سوالات مربوط به دروس مختلف را دریافت کنند.
- **ویدئوهای آموزشی:** ویدئوهای آموزشی مرتبط با دروس نقشه‌برداری در دسترس هستند.
- **اطلاعیه‌ها:** آخرین اخبار و اطلاعیه‌های انجمن علمی از طریق ربات ارسال می‌شود.
- **پشتیبانی:** در صورت وجود هرگونه مشکل یا سوال، دانشجویان می‌توانند از طریق ربات با تیم پشتیبانی در ارتباط باشند.

---

## 🚀 نحوه استفاده از ربات

1. **شروع کار:** برای شروع کار با ربات، دستور `/start` را ارسال کنید.
2. **انتخاب درس:** از بین لیست دروس ارائه شده، درس مورد نظر خود را انتخاب کنید.
3. **انتخاب نوع منبع:** پس از انتخاب درس، می‌توانید نوع منبع (جزوه، نمونه سوال، ویدئو) را انتخاب کنید.
4. **دریافت فایل:** ربات فایل‌های مربوطه را برای شما ارسال می‌کند.

---

## 📂 ساختار پروژه

- **`main.py`:** فایل اصلی ربات که منطق ربات در آن پیاده‌سازی شده است.
- **`Users.db`:** پایگاه داده SQLite که اطلاعات کاربران و تاریخچه استفاده از ربات را ذخیره می‌کند.
- **`README.md`:** این فایل که توضیحات پروژه را ارائه می‌دهد.
- **`requirements.txt`:** لیست کتابخانه‌های مورد نیاز برای اجرای پروژه.

---

## 🛠️ راه‌اندازی پروژه

برای راه‌اندازی ربات بر روی سیستم خود، مراحل زیر را دنبال کنید:

### پیش‌نیازها

- Python 3.8 یا بالاتر
- کتابخانه `python-telegram-bot`

### نصب کتابخانه‌ها

کتابخانه‌های مورد نیاز را با استفاده از دستور زیر نصب کنید:

```bash
pip install -r requirements.txt
