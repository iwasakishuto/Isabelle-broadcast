# coding: utf-8
import sys
import argparse
from imgcat import imgcat
from main import (create_img, get_default_text, 
                  DEFAULT_BGIMG_PATH, DEFAULT_FONT_PATH)

class ListParamProcessor(argparse.Action):
    def __call__(self, parser, namespace, values, option_strings=None):
        setattr(namespace, self.dest, [int(e) for e in values[1:-1].split(",")])

def isacast(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(prog="isacast", add_help=True)
    parser.add_argument("-T",  "--text",       type=str,                  default=get_default_text())
    parser.add_argument("-BB", "--text-box",   action=ListParamProcessor, default=(450, 720, 1500, 970))
    parser.add_argument("-FC", "--text-rgb",   action=ListParamProcessor, default=(114, 109, 88))
    parser.add_argument("-F",  "--ttfontpath", type=str,                  default=DEFAULT_FONT_PATH)
    parser.add_argument("-FS", "--fontsize",   type=int,                  default=60)
    parser.add_argument("--bg-img",            type=str,                  default=DEFAULT_BGIMG_PATH)
    parser.add_argument("-BC", "--bg-rgb",     action=ListParamProcessor, default=(255, 247, 225))
    parser.add_argument("--save",              action="store_true")
    args = parser.parse_args(argv)
    
    img = create_img(
        text=args.text.replace("\\n", "\n"), textBox=args.text_box, textRGB=args.text_rgb,
        ttfontpath=args.ttfontpath, fontsize=args.fontsize,
        backgroundIMG=args.bg_img, backgroundRGB=args.bg_rgb
    )
    imgcat(img)

    if args.save:
        img.save("Isabelle-broadcast.png")
