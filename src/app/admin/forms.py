from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class CatalogItemForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired()]),
    description = StringField('Description', validators=[DataRequired()]),
    image_url = StringField('Image Upload', validators=[DataRequired()]),
    price = DecimalField('Price', validators=[DataRequired()]),
    is_sale_item = BooleanField('Is Sale Item', validators=[DataRequired()]),
    submit = SubmitField('Upload')

class CategoryForm(FlaskForm):
    name= StringField('Caption', validators=[DataRequired()])
    submit = SubmitField('Upload')
