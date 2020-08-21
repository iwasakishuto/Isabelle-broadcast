# coding: utf-8
# Author iwasakishuto
# Date 2020-06-21
import os
from PIL import Image, ImageDraw, ImageFont
from imgcat import imgcat
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FONT_PATH  = os.path.join(HERE, "font/07やさしさゴシックボールド.ttf")
DEFAULT_BGIMG_PATH = os.path.join(HERE, "image/background.png")

# Datetime Functions.
# @params dt: <class 'datetime.datetime'>
get_day_of_week_jp = lambda dt: ["月", "火", "水", "木", "金", "土", "日"][dt.weekday()]
get_greeting_msg   = lambda dt: "おはようございます" if 5 <= dt.hour < 12 else "こんにちは" if dt.hour < 19 else "こんばんは"
get_ampm_jp        = lambda dt: "午後" if dt.strftime("%p")=="PM" else "午前"
get_text_from_dt   = lambda dt: dt.strftime(f"みなさ〜ん、{get_greeting_msg(dt)}！\nただいまの　時刻は\n%Y年  %m月  %d日  {get_day_of_week_jp(dt)}曜日の\n{get_ampm_jp(dt)}%I時%M分です")
def get_default_text():
    dt = datetime.now()
    return get_text_from_dt(dt)

def create_img(text=get_default_text(),  textBox=(450, 720, 1500, 970), textRGB=(114, 109, 88),
               ttfontpath=DEFAULT_FONT_PATH, fontsize=60,
               backgroundIMG=DEFAULT_BGIMG_PATH, backgroundRGB=(255, 247, 225)):
    left, upper, right, lower = textBox
    textWidth = right-left; textHeigh = lower-upper
    canvasSize = (textWidth, textHeigh)

    text_img = Image.new(mode="RGB", size=canvasSize, color=backgroundRGB)
    draw = ImageDraw.Draw(im=text_img)
    font = ImageFont.truetype(font=ttfontpath, size=fontsize)
    draw.text(xy=(0, 0), text=text, fill=textRGB, font=font)

    bg_img = Image.open(fp=backgroundIMG)
    bg_img.paste(im=text_img, box=textBox[:2])
    return bg_img

if __name__ == "__main__":
    img = create_img()
    imgcat(img)
    # img.save("Isabelle-broadcast.png")

