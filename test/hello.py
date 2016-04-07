__author__ = 'root'

import os

from flask import Flask
from flask import request

from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

from flask import render_template

from flask.ext.moment import Moment

from flask import session,redirect,url_for

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'that is really hard!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)


class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/',methods=['GET','POST']) 
def index():
    # return render_template('index.html',current_time=datetime.utcnow())
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        # name = form.name.data
        # form.name.data = ''
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))
# @app.route('/')
# def index():
#     response = make_response('<h1>This ducument is a cookie<h1>')
#     response.set_cookie('answer','42')
#     return response

@app.route('/<name>')
def user(name):
    # return '<h1>hello %s<h1>' % name
    return render_template('user.html',name=name)

@app.route('/user_agent')
def userAgent():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s<br>' % user_agent

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__=='__main__':
    manager.run()

