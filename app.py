from flask import Flask, render_template, request
import cv2
from keras.models import load_model
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from PIL import Image
from predict import *
from labels import *
from scraping import *
import urllib
from wiki_urls import *

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET', 'POST'])
def after():
    img = request.files['file_input']

    img.save('static/file.jpg')

    model, input_details, output_details = load_model()
    image = Image.open("static/file.jpg")
    model_output = run_inference(model, image, input_details, output_details)
    answer=np.argmax(model_output, axis=-1)
    name = labels[answer[0]]
    url = all_urls[answer[0]]
    description, info = parse(url)

    # urllib.request.urlretrieve( 'image_full_url', 'static/bird_img.jpg')

    return render_template('after.html', name = name, len = len(info), info = info, desc = description)
 

if __name__ == "__main__":
    app.run(debug=True)
