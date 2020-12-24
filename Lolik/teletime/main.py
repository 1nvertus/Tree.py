from telethon import TelegramClient, cync
from telethon.tl.functions.photos import UploadProfilePhotoRequests, DeletePhotosRequests
from datetime import datetime
import time
from config import *
from time_pic import *

client = TelegramClient('ananas', api_id, api_hash)
client.start()


while True:
	#меняет картинки
	change_img()
	#удаляет картинку из телеги
	client(DeletePhotosRequests(client.get_profile_photos('me')))
	#храниться картинка
	file = client.upload_file(f"time.png")
	#загружает картинку из телеги
	client(UploadProfilePhotoRequests(file))
	#каждые 1 минменяет картинку
	time.sleep(30)
	
