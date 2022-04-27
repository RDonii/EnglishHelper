# Telegram Bot 

[Read this in English](https://github.com/RDonii/EnglishHelper#english)
## Uzbek
### Umumiy ma'lumot
Foydalanuvchi yuborgan matinni ingliz tilidan o'zbek tiliga yoki o'zbek tilidan ingliz tiliga tarjima qilib beradi. Agarda bitta ingliz tilida so'z yuborilsa shu so'zning to'liq ta'rifi va uni talaffuz qilinishlari haqida ma'lumot beradi.

### Ishga tushirish
Botni ishga tushirish uchun sizga developer.oxforddictionaries.com saytidan, @BotFather va @userinfobot telegram botidan olingan quyidagi mahfiy qiymatlar kerak bo'ladi. .env faylini yaratib, jadvaldagi nomlar bilan saqlab qo'yish lozim.

| Nomi  | Qayerdan | .env nomi |
| ------------- | ------------- | ------------- |
| Bot token  | @BotFather  | BOT_TOKEN |
| Admin user id  | @userinfobot  | ADMINS |
| app id | peveloper.oxforddictionaries.com  | APP_ID |
| app key | peveloper.oxforddictionaries.com  | APP_KEY |

Python tilining yangi versiyalaridan birini o'rnatib bo'lgach, `pip install -r requirements.txt` buyrug'i yordamida kerakli modullar o'rnatiladi.

So'ngra, `python app.py` orqali bot ishga tushiriladi.

## English
[O'zbek tilida o'qish](https://github.com/RDonii/EnglishHelper#uzbek)
### General information
Translates the submitted text from English into Uzbek or from Uzbek into English. If a word is sent in English, it gives a complete definition of the word and how it is pronounced.

### Dependencies
To run the bot, you will need special values from peveloper.forddictionaries.com website, @BotFather and @userinfobot telegram bots. Create an .env file and save it with the names shown in the table.

| name  | Where | in .env |
| ------------- | ------------- | ------------- |
| Bot token  | @BotFather  | BOT_TOKEN |
| Admin user id  | @userinfobot  | ADMINS |
| app id | peveloper.oxforddictionaries.com  | APP_ID |
| app key | peveloper.oxforddictionaries.com  | APP_KEY |

After installing one of the newer versions of Python, the required modules are installed using the command `pip install -r requirements.txt`.

Then the bot is launched with the commad `python app.py`.
