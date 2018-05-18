# -*- coding:utf-8 -*-

import os

from PIL import Image, ImageDraw, ImageFont
from flask import render_template, request, redirect, url_for, abort

from app import app, photos

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
outfile = r"E:/flask_grey/"


@app.route('/')
def hello_world():
    return render_template('pic/pic_upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        im = Image.open(request.files['photo'])
        im = im.resize((80, 80), Image.NEAREST)
        txt = ''

        for i in range(80):
            for j in range(80):
                txt += get_char(*im.getpixel((j, i)))
            txt += '\n'
        print(txt)
        asc_im = Image.new("RGB", (1000, 1000), (255, 255, 255))
        dr = ImageDraw.Draw(asc_im)
        font = ImageFont.truetype(os.path.join("fonts", "msyh.ttf"), 14)
        dr.text((0, 0), txt, font=font, fill="#000000")
        if not os.path.exists(outfile):
            os.makedirs(outfile)
        asc_im.save(outfile + filename)

        return redirect(url_for('show', name=filename))
    return render_template('pic/pic_upload.html')


@app.route('/pic/<name>')
def show(name, txt):
    if name is None:
        abort(404)
    url = photos.url(name)
    return render_template('pic/pic_show.html', **locals())


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    app.run(host='localhost', port=8097)
