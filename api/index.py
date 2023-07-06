# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write('Hello, world!'.encode('utf-8'))
#         return

import telegram
from telegram.constants import ParseMode
from telegram.ext import Updater

TELEGRAM_TOKEN = '6285893081:AAGOc4qvbvpGV6t7pYyevV01Qz9fdmEn4sY'  # Thay đổi token của bot Telegram
CHAT_ID = '-1001946459218'  # Thay đổi chat_id của bạn

async def send_to_telegram(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.MARKDOWN)

send_to_telegram('⌚️ Xin chào! Đây là tin nhắn lúc 8h30 hàng ngày nhé ⌚️')
