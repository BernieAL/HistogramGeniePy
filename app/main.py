

# https://roytuts.com/upload-and-display-image-using-python-flask/
# https://roytuts.com/upload-and-display-multiple-images-using-python-and-flask/



import os
from flask import Flask, jsonify, render_template,request
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS





from img_processing_logic import run_img


UPLOAD_FOLDER = 'app/static/uploads'
app = Flask(__name__)
CORS(app)
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
    
    print(request)
    # """If file attribute not on reqeust"""
    # if 'file' not in request.files:
    #     flash('NO file part')
    #     return redirect(request.url)
    
    # file = request.files['file']
    # # file = file.resize(150,100),Image.ANTIALIAS)
    # if file.filename == '':
    #     flash('No image for uploading')
    #     return redirect(request.url)

    # """
    # if file is populated and is of allowed type
    # Pass it a filename and it will return a secure version of it. 
    # This filename can then safely be stored on a regular file system and passed to os.path.join()
    # save file to upload folder
    # render upload.html and pass it the filename
    # """
    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     img_file = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    #     file.save(img_file)
        
        
        
    #     #pass path to run_img function
    #     paletteColors,complementary_colors = run_img.run_main(img_file)
    #     # print(f"Original palette {paletteColors}")
    #     # print(f"comeplementary_colors {complementary_colors}")
    #     colors = {
    #         'palette':paletteColors,
    #         'complementary': complementary_colors
    #     }

    #     # #pass dominate colors as array to template for dynamic rendering as inline css
    #     # return render_template('upload.html',filename=filename,palette = paletteColors,
    #     #     comeplementary_colors=complementary_colors,colors = json.dumps(colors))

    #     return jsonify(colors)
        
    return ('you did it.')
    
    # else:
    #     flash('Image submitted is not allowed file type')
    #     return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
        return redirect(url_for('static', filename='uploads/'+filename),code=301)



if __name__ == '__main__':
		app.run(debug=True)
	