import telebot
import random
import string

TOKEN = "8802912711:AAHcZSa_3f1y2wcBQNstWTrBlYQch-r_iQ8"

bot = telebot.TeleBot(TOKEN)

# danh sách tỉnh/thành
provinces = [
    "HANOI",
    "HAIPHONG",
    "DANANG",
    "HAGIANG",
    "CAOBANG",
    "LAOCAI",
    "YENBAI",
    "TUYENQUANG",
    "LANGSON",
    "BACNINH",
    "QUANGNINH",
    "HAIDUONG",
    "HUNGYEN",
    "NAMDINH",
    "THAIBINH",
    "NINHBINH",
    "THANHHOA",
    "NGHEAN",
    "HATINH",
    "QUANGBINH",
    "QUANGTRI",
    "HUE",
    "QUANGNAM",
    "QUANGNGAI",
    "BINHDINH",
    "PHUYEN",
    "KHANHHOA",
    "NINHTHUAN",
    "BINHTHUAN",
    "KONTUM",
    "GIALAI",
    "DAKLAK",
    "DAKNONG",
    "LAMDONG",
    "BINHDUONG",
    "DONGNAI",
    "TAYNINH",
    "LONGAN",
    "TIENGIANG",
    "BENTRE",
    "VINHLONG",
    "CANTHO",
    "ANGIANG",
    "KIENGIANG",
    "CAMAU",
    "SOCTRANG",
    "TRAVINH",
    "BACLIEU"
]

# random user 6-10 ký tự
def random_username():

    length = random.randint(6, 10)

    chars = string.ascii_lowercase + string.digits

    return ''.join(random.choice(chars) for _ in range(length))

# random pass 6-8 ký tự
def random_password():

    length = random.randint(6, 8)

    chars = string.ascii_letters + string.digits

    return ''.join(random.choice(chars) for _ in range(length))

# random số điện thoại
def random_phone():

    return "0" + ''.join(random.choice(string.digits) for _ in range(9))

@bot.message_handler(func=lambda m: True)
def handle(message):

    try:

        text = message.text.strip()

        parts = text.split()

        stk_index = -1

        # tìm STK
        for i, part in enumerate(parts):

            if part.isdigit():

                stk_index = i

                break

        if stk_index == -1:

            bot.reply_to(message, "Không tìm thấy STK")

            return

        # họ tên
        name = ' '.join(parts[:stk_index])

        # STK
        stk = parts[stk_index]

        # ngân hàng
        bank = ''.join(parts[stk_index + 1:]).upper()

        # random chi nhánh
        province = random.choice(provinces)

        # random user
        username = random_username()

        # random pass
        password = random_password()

        # ngày sinh ngắn
        birthday_short = "050190"

        # sđt
        phone = random_phone()

        # email
        email = f"{username}@gmail.com"

        # ngày sinh đầy đủ
        birthday_full = "1990/01/05"

        # kết quả
        result = f"{name}|{stk}|{bank}|{province}|{username}|{password}|{birthday_short}|{phone}|{email}|{birthday_full}"

        bot.reply_to(message, result)

    except Exception as e:

        bot.reply_to(message, f"Lỗi: {e}")

print("BOT DANG CHAY...")

bot.infinity_polling()