from flask import Flask, request, jsonify
import cv2
import os

app = Flask(__name__)

test = {
    'coba': 'testing'
}


@app.route('/test', methods=['GET'])
def testing():
    return test

@app.route('/get_gambar', methods=['GET'])
def get_data():
    img_path = os.listdir('images')
    img = cv2.imread('images/'+img_path)
    return img

@app.route('/post_gambar', methods=['POST'])
def post_gambar():
    img = request.form['img_name']
    cv2.imwrite('images/'+img)
    return img

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5000)

