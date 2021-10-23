

# https://roytuts.com/upload-and-display-image-using-python-flask/
# https://roytuts.com/upload-and-display-multiple-images-using-python-and-flask/



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
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

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
    

    """If file attribute not on reqeust"""
    if 'file' not in request.files:
        flash('NO file part')
        return redirect(request.url)
    
    file = request.files['file']

    if file.filename == '':
        flash('No image for uploading')
        return redirect(request.url)

    """
    if file is populated and is of allowed type
    Pass it a filename and it will return a secure version of it. 
    This filename can then safely be stored on a regular file system and passed to os.path.join()
    save file to upliad folder
    render upload.html and pass it the filename
    """
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        
        #pass path to run_img function
        run_img.run_img_func(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return render_template('upload.html',filename=filename)
    
    else:
        flash('Image submitted is not allowed file type')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
        return redirect(url_for('static', filename='uploads/'+filename),code=301)



if __name__ == '__main__':
		app.run(debug=True)
	