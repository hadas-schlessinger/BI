from flask import  render_template, request
from werkzeug.utils import secure_filename
from app import app
import sys
import os
import flask_executor
from flask import send_file

@app.route('/airports', methods=['POST', 'GET'])
def airports():
    try:
        return send_file('/app/static/react/logo512.png',
                         attachment_filename='python.jpg')
    except Exception as e:
        return str(e)


@app.route('/ports', methods=['POST', 'GET'])
def ports():
    try:
        return send_file('/app/static/react/logo512.png',
                         attachment_filename='python.jpg')
    except Exception as e:
        return str(e)

@app.route('/popularity', methods=['POST'])
def popularity():
    try:
        return send_file('/app/static/react/logo512.png',
                         attachment_filename='python.jpg')
    except Exception as e:
        return str(e)


# @app.route('/generate', methods=['POST'])
# def generate():
#     logging.info(f'got a request {request.form}')
#     name = request.form.get('name_data')
#     if name == '':
#         return json.dumps({"error": 'please insert your data and project name'}), 400
#     id = request.form.get('id')
#     if id not in os.listdir('static'):
#         logging.warning(f'invalid id {id}, returning error')
#         return json.dumps({"error": 'invalid name'}), 400
#     id = {'id': id,
#          'status': 'PENDING'}
#     luminex = request.form.get('luminex') in ['true', '1', 'True', 'TRUE', 'on']
#     log_transform = request.form.get('log_transform') in ['true', '1', 'True', 'TRUE', 'on']
#     outcomes = request.form.get('outcomes')
#     covariates = request.form.get('covariates')  # names of regression covariates to control for
#     log_column_names = request.form.get('log_column_names')
#     cytokines = request.form.get('cytokines', default='') # if none, will analyze all
#     parameters = [name, id, request.form.get('name_compartment', default='Compartment'), luminex, log_transform, request.form.get('max_testing_k', type=int, default=6),
#                   False, outcomes.split(", "), covariates.split(", "), log_column_names.split(", ") , cytokines.split(", ")
#                   ]
#     method = threading.Thread(target=server_tools.run_server, args=(parameters))
#     method.daemon = True
#     method.start()
#     logging.info(f'Tread {method.name} started running and calculating the method')
#     return {'id': id}




# if __name__ == "__main__":
#     app.run(ssl_context=('cert.pem', 'key.pem'))