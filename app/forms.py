from flask_wtf import FlaskForm
from wtforms import FileField, validators


class UploadForm(FlaskForm):
    fileUpload = FileField("Upload Images", description="jpg/png files only", validators=[validators.regexp('^\\[^/\\]\.jpg$'), validators.regexp('^\\[^/\\]\.png$')])