from PIL import Image
from flask import Blueprint, render_template, request, jsonify
from models import FaceNetModel

base = Blueprint('base', __name__)


@base.route('/')
def index():
    return render_template('index.html')


@base.route('/predict', methods=['post'])
def predict():
    files = request.files
    imgLeft = Image.open(files.get('imgLeft'))
    imgRight = Image.open(files.get('imgRight'))
    imgLeft.save('imgLeft.jpg')
    imgRight.save('imgRight.jpg')
    return jsonify(same=True, score=0.3, imgLeft='imgLeft' in files, imgRight='imgRight' in files)
