# coding: utf-8
# Author iwasakishuto
# Date 2020-06-21
import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

BASE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR_PATH)

def get_day_of_week_jp(dt):
    return ["月", "火", "水", "木", "金", "土", "日"][dt.weekday()]

def get_greeting_msg(dt):
    return "おはようございます" if 5 <= dt.hour < 12 else "こんにちは" if dt.hour < 19 else "こんばんは"

def get_ampm_jp(dt):
    return "午後" if dt.strftime("%p")=="PM" else "午前"

def get_text():
    dt = datetime.now()
    text = f"""みなさ〜ん、{get_greeting_msg(dt)}！
ただいまの　時刻は
%Y年  %m月  %d日  {get_day_of_week_jp(dt)}曜日の
{get_ampm_jp(dt)}%I時%M分です"""
    return dt.strftime(text)

def create_text_img(text=get_text(), ttfontname="font/07やさしさゴシックボールド.ttf", fontsize=60):
    backgroundRGB = (255, 247, 225)
    textRGB       = (114, 109, 88)

    textBox = (450, 720, 1500, 970)
    left, upper, right, lower = textBox
    textWidth, textHeigh = right-left, lower-upper
    canvasSize = (textWidth, textHeigh)

    text_img = Image.new(mode="RGB", size=canvasSize, color=backgroundRGB)
    draw = ImageDraw.Draw(im=text_img)
    font = ImageFont.truetype(font=ttfontname, size=fontsize)
    draw.text(xy=(0, 0), text=text, fill=textRGB, font=font)

    base_img = Image.open(fp="image/background.png")
    base_img.paste(im=text_img, box=textBox[:2])
    return base_img

if __name__ == "__main__":
    img = create_text_img()
    img.save("Isabelle-broadcast.png")

