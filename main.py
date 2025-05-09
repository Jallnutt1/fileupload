from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os 
from wtforms.validators import InputRequired
from dotenv import load_dotenv
# Hello World

app = Flask(__name__, instance_relative_config=True)

# app.config["SECRET_KEY"] <- This doesn't work with storing secrets in .env
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

# @app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    uploaded = os.listdir(app.config['UPLOAD_FOLDER'])
    if form.validate_on_submit():
        file = form.file.data
        # print(file)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        uploaded = os.listdir(app.config['UPLOAD_FOLDER'])

        return render_template('index.html', form=form, files=uploaded)
    return render_template('index.html', form=form, files=uploaded)

@app.route('/delete/<fileD>', methods=['GET', 'POST'])
def delete(fileD):
    os.remove('/Users/analyst/Documents/development/fileUpload/static/files/' + fileD)
    # print('/Users/analyst/Documents/development/fileUpload/static/files' + fileD)
    return redirect('/')
    


if __name__ == '__main__':
    app.run(debug=True)





#.env (using python-dotenv) stores secret keys
# gunicorn fur:app <-- w/ __init__.py file
# gunicorn main:app <-- inside of fir, __init__.py -> main.py

# https://youtu.be/GeiUTkSAJPs?si=F5JPGzrzV7FsQJA9&t=593

# sam - nfs

     