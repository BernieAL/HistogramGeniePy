
import os
from flask import Flask, render_template,request
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename




from img_processing_logic import run_img


UPLOAD_FOLDER = 'app/static/uploads'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/')
# def index():
#     return render_template("base.html")

@app.route('/')
def upload_form():
	return render_template('upload.html')


@app.route('/',methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('NO FILE')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename =='':
        flash('No image selected for upliading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        
        return render_template('upload.html',filename = filename)
    else:
        flash('Image type not allowed')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: '+ filename)
    run_img.run_img_func(filename)
    return redirect(url_for('static',filename='uploads/'+filename),code = 301)

if __name__ == '__main__':
		app.run(debug=True)
	