import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 50
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
KIEV_UTC = 4 #часовой пояс

def convert_time_to_string(dt):
	'''Обновляет время по Киеву и возвращает строку'''
	dt += timedelta(hours=KIEV_UTC)
	return f"{dt.hour}:{dt.minute:02}"
def change_img():
	'''Шаманит с нашей фоткой'''
	#стартует время
	start_time = datetime.utcnow()
	#превращает ддату в строку
	text = convert_time_to_string(start_time) 
	#
	row = Image.new('RGBA', (200, 200), "black")
	parsed = ImageDraw.Draw(row)
	font = ImageFont.truetype("название шрифта",FONT_SIZE)
	
	
