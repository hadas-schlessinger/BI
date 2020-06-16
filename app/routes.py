import base64
from flask import request
from app import app
from .backend import calculatioins


@app.route('/airports', methods=['POST', 'GET'])
def airports():
    # calculatioins.generate_airports(False)
    image = _encode_image('static/airports.png')
    return {'data': str(image)}


@app.route('/routes', methods=['POST', 'GET'])
def routes():
    airport = request.form.get('airport')
    destiinations= calculatioins.generate_routes(airport)
    image = _encode_image('static/routes.png')
    return {'data': str(image),
            'destinations': destiinations,
            'total': len(destiinations)}

@app.route('/popularity', methods=['POST'])
def popularity():
    calculatioins.generate_popularity()
    image = _encode_image('static/airports.png')
    image_p = _encode_image('./top_10.png')
    return {'data': str(image),
            'priority': str(image_p)}


def _encode_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

