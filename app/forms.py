from flask_wtf import FlaskForm
from wtforms import FileField, validators


# validators=[validators.regexp('^\\[^/\\]\.jpg$'), validators.regexp('^\\[^/\\]\.png$')]

class UploadForm(FlaskForm):
    fileUpload = FileField("Upload Image", description="jpg/png files only")