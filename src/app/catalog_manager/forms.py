from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class CatalogItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    image_url = StringField('Image Upload', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    category_id = IntegerField('Category Id', validators=[DataRequired()])
    submit = SubmitField('Save')