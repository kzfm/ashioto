from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from ashioto.track.database import Base
from datetime import datetime


class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    name = Column(Text)
    lastplay = Column(DateTime, default=datetime.now())
    times = Column(Integer)

    def __init__(self, title=None, name=None, lastplay=None, times=1):
        self.title = title
        self.name = name
        self.lastplay = lastplay
        self.times = times

    def __repr__(self):
        return '<Title {} - {}>'.format(self.title, self.name)


class Chain(Base):
    __tablename__ = 'chain'
    __table_args__ = (UniqueConstraint('head', 'tail'), {})
    id = Column(Integer, primary_key=True)
    head = Column(Integer, ForeignKey('track.id'))
    tail = Column(Integer, ForeignKey('track.id'))
    times = Column(Integer)

    def __init__(self, head=None, tail=None, times=1):
        self.head = head
        self.tail = tail
        self.times = times
