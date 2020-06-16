from flask import  render_template, request
from werkzeug.utils import secure_filename
from app import app
import base64
from .backend import calculatioins
import threading

@app.route('/airports', methods=['POST', 'GET'])
def airports():
    # method = threading.Thread(target=calculatioins.generate_airports())
    # method.daemon = True
    # method.start()

    calculatioins.generate_airports()
    image = _encode_image('app/world.jpg')
    return {'data': str(image)}


@app.route('/routes', methods=['POST', 'GET'])
def routes():
    calculatioins.generate_routes()
    image = _encode_image('app/static/react/logo192.png')
    return {'data': str(image)}

@app.route('/popularity', methods=['POST'])
def popularity():
    calculatioins.generate_popularity()
    image = _encode_image('app/static/react/logo192.png')
    return {'data': str(image)}



def _encode_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

