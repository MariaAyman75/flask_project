from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from app.models import Creator, db


class postForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(2, 40)])
    description = StringField("Description")
    image= FileField("Image") 
    creator_id = SelectField("Creator", validators=[DataRequired()], choices=[])
    submit = SubmitField("submit")

    def __init__(self, *args, **kwargs):
        super(postForm, self).__init__(*args, **kwargs)
        self.creator_id.choices = [(c.id, c.name) for c in Creator.query.all()]