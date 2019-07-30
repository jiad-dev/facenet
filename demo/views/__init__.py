from PIL import Image
from flask import Blueprint, render_template, request, jsonify

import demo
from demo.boot import app

base = Blueprint('base', __name__)


@base.route('/')
def index():
    return render_template('index.html')


@base.route('/predict', methods=['post'])
def predict():
    files = request.files
    img_left = Image.open(files.get('imgLeft'))
    img_right = Image.open(files.get('imgRight'))
    distance, similar = demo.is_same(img_left, img_right)
    model_name = app.config['USE_MODEL']
    model_acc = demo.ModelLoaded.acc
    return jsonify(same=bool(similar), score=distance.item(), model_name=model_name, model_acc=model_acc)
