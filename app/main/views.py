#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from datetime import datetime
from flask import render_template,session,redirect,url_for,flash

from . import main
from .forms import NameForm,MailForm
from .. import db
from ..models import User

from ..email import send_email
from flask.ext.mail import Message,Mail
from flask import Flask
# from app import mail

from flask.ext.login import login_required

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',form = form,name = session.get('name'),known = session.get('known',False),current_time = datetime.utcnow())
#
@main.route('/testsendemail',methods=['GET','POST'])
def test_send_email():
    mailForm= MailForm()
    if mailForm.validate_on_submit():#表单提交成功的判断
        try:
            app = Flask(__name__)
            app.config['SECRET_KEY'] = 'qiyeboy'
            #下面是SMTP服务器配置
            app.config['MAIL_SERVER'] = 'smtp.163.com' #电子邮件服务器的主机名或IP地址
            app.config['MAIL_PORT'] = '25' #电子邮件服务器的端口
            app.config['MAIL_USE_TLS'] = True #启用传输层安全
            app.config['MAIL_USERNAME'] ='13259744109@163.com' #os.environ.get('MAIL_USERNAME') #邮件账户用户名
            app.config['MAIL_PASSWORD'] = 'hywd1993'#os.environ.get('MAIL_PASSWORD') #邮件账户的密码

            mail = Mail(app)
            receiverName = mailForm.receiver.data #收件人文本框的内容
            styledata = mailForm.style.data#主题文本框的内容
            bodydata  = mailForm.body.data#正文文本框的内容
            msg = Message(styledata,sender='13259744109@163.com',recipients=[receiverName])#发件人，收件人
            msg.body = bodydata
            # send_email('2531145412@qq.com','Test email-function',)
            mail.send(msg)
            flash('邮件发送成功!')#提示信息
            return redirect(url_for('.index'))
        except:
            flash('邮件发送失败!')
            return redirect(url_for('.index'))
    return render_template('testemail.html',form=mailForm,name ='13259744109@163.com' )#渲染网页



# @main.route('/secret')
# @login_required
# def secret():
#     return 'Only authenticated users are allowed!'