from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash, jsonify
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager, Shell
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

Bootstrap(app)
Moment(app)
db = SQLAlchemy(app)
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))


migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return 'The browse is %s' % user_agent

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie.</h1>')
#     response.set_cookie('secret', '007')
#     print(response.__dict__)
#     return response


class NameForm(FlaskForm):
    name = StringField('What is your name', validators=[Required()])
    submit = SubmitField('Submit')


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed name')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, current_date=datetime.utcnow(), name=session.get('name', ''), known=session.get('known', False))

@app.route('/baidu/')
def baidu():
    return redirect('/web/login/')

@app.route('/web/login/')
def login():
    return '<h1>Login success!!!</h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'yiji':
        return '<h1>Bad Request</h1>', 404
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500