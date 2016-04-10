#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Email

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')


class MailForm(Form):
    receiver = StringField('收件人:',validators=[Required(),Email()])
    style = StringField('主题:',validators=[Required()])
    body = TextAreaField('正文:',validators=[Required()])
    submit = SubmitField('发送')