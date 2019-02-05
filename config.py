import os


class Config(object):
    FLASK_DEBUG = True  # Do not use debug mode in production

    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite')
    db_uri = 'sqlite:///{}'.format(db_path)
#
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
