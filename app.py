import os
from flask import Flask, render_template, request
from crack_detector import is_cracked

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
                image.save(image_path)

                result = is_cracked(image_path)

                os.remove(image_path)

                return result

    return render_template('index.html')


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)

