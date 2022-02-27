from flask_wtf import FlaskForm
from wtforms import FileField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    fileUpload = FileField("Upload Image", description="jpg/png files only", validators=[FileRequired("A file is required to continue"), FileAllowed(['jpg', 'png', 'jpeg', 'Image files only jpg/png files only'])])