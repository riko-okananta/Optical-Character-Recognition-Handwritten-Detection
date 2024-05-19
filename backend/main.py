from flask import Flask, request, jsonify
import cv2
import os

app = Flask(__name__)

test = {
    'coba': 'testing'
}


@app.route('/test', methods=['GET'])
def testing():
    return jsonify(test)

@app.route('/get_gambar', methods=['GET'])
def get_data():
    img_path = os.listdir('images')
    img = cv2.imread('images/'+img_path)
    return img

@app.route('/post_gambar', methods=['POST'])
def post_gambar():
    file = request.files['file']
    if 'file' not in request.files:
        return "No File part", 400

    if file.filename == '':
        return "No Selected file", 400

    if file:
        filename = file.filename
        img_path = os.path.join('images/'+filename)
        file.save(img_path)
        return f"File {filename} uploaded successfully", 201

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True, port=5000)

