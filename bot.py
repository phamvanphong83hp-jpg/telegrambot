import telebot
import random
import string

TOKEN = "TOKEN_BOT_CUA_BAN"

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

# tạo username theo tên
def create_username(name):

    parts = name.lower().split()

    first = parts[-1]

    middle = parts[-2] if len(parts) >= 2 else ""

    number = ''.join(random.choice(string.digits) for _ in range(2))

    suffix = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))

    return f"{first}{middle}{number}{suffix}"

# tạo password theo tên
def create_password(name):

    parts = name.lower().split()

    first = parts[-1]

    last = parts[0]

    number = ''.join(random.choice(string.digits) for _ in range(3))

    return f"{first}{last}{number}"

# random 6 số
def random_six():

    return ''.join(random.choice(string.digits) for _ in range(6))

# random số điện thoại Việt Nam chuẩn
def random_phone():

    prefixes = [
        "032", "033", "034", "035", "036", "037", "038", "039",
        "070", "076", "077", "078", "079",
        "081", "082", "083", "084", "085",
        "056", "058",
        "086", "088", "089",
        "090", "091", "092", "093", "094",
        "096", "097", "098", "099"
    ]

    prefix = random.choice(prefixes)

    remain = ''.join(random.choice(string.digits) for _ in range(7))

    return prefix + remain

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

        # chi nhánh random
        province = random.choice(provinces)

        # user
        username = create_username(name)

        # pass
        password = create_password(name)

        # 6 số random
        birthday_short = random_six()

        # số điện thoại
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