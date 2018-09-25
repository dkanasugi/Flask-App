#Daichi Kanasugi
#This program uses flask and flask_bootstrap to host a local webserver
#It displays the type, pixel size, and mode of a random image chosen by
#random module. Main page will display 3 random picture.
#It uses main.html, picture.html, and image_info

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
from PIL import Image
from image_info import image_info

app = Flask(__name__)
bootstrap = Bootstrap(app)

global index1
global index2
global index3

#main.html
@app.route('/')
def main():
    index1 = random.randint(0,9)
    name1 = image_info[index1]['id_1']
    title1 = image_info[index1]['title']

    index2 = random.randint(0,9)
    name2 = image_info[index2]['id_1']
    title2 = image_info[index2]['title']

    index3 = random.randint(0,9)
    name3 = image_info[index3]['id_1']
    title3 = image_info[index3]['title']
    return render_template('main.html', name1 = name1,name2 = name2,name3 = name3,title1 = title1,title2 = title2,title3 = title3)

#picture.html
@app.route('/picture/<id>')
def picture(id):
    for image in image_info:
        if image['id_1'] == id:
            id_1 = image['id_1']
            title = image['title']
            flickr_user = image['flickr_user']

            img = Image.open("static/"+id_1+".jpg")
            mode = img.mode
            format = img.format
            width, height = img.size

    return render_template("picture.html", picId_1 = id_1, title_1 = title, flickr_user_1 = flickr_user, width = width, height = height, mode = mode, format = format)
