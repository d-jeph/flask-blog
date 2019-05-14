import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '63NYIZDIyNNZ27UAsoNI5lpD2i09ncYf'

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #mail config
    MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'jkimanthi01@gmail.com',
	MAIL_PASSWORD = '#kima2010'

    POSTS_PER_PAGE = 3
