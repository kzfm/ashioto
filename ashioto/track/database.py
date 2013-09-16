from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

home = os.path.expanduser("~")
database_file = os.path.join(home, '.ashioto', 'ashioto.db')
engine = create_engine('sqlite:///' + database_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import ashioto.track.models
    Base.metadata.create_all(bind=engine)
