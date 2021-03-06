

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
        img_file = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(img_file)
        
        
        #pass path to run_img function
        #get returned dominate colors value(s) from run_main, store in colors object
        #colors is an object that has dom and comp colors nested
        #dom and comp colors are arrays of arrays
        colors = run_img.run_main(img_file)
        
        dom_colors1 = colors['dominant'][0]
        dom_colors2 = colors['dominant'][1]

        comp_colors1 = colors['complimentary'][0]
        comp_colors2 = colors['complimentary'][1]
        
        print(dom_colors1)
        print(dom_colors2)
        print(comp_colors1)
        print(comp_colors2)

        
        
        #pass dominate colors as array to template for dynamic rendering as inline css
        return render_template('upload.html',filename=filename)
    
    else:
        flash('Image submitted is not allowed file type')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
        return redirect(url_for('static', filename='uploads/'+filename),code=301)



if __name__ == '__main__':
		app.run(debug=True)
	