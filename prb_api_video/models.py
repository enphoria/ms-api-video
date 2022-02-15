from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import *
from prb_api_video.ext.database import db
from sqlalchemy.orm import relationship


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))

class Person(db.Model, SerializerMixin):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    cellphone = db.Column(db.BigInteger)
    city = db.Column(db.String(200))
    locality = db.Column(db.String(200))
    subject_interest_id = db.Column(db.Integer, ForeignKey('subject_interest.id'))
    person_video_id = db.Column(db.Integer,  ForeignKey('person_video.id'))
    subject_interest = relationship('SubjectInterest')
    person_video = relationship('PersonVideo')

class SubjectInterest(db.Model, SerializerMixin):
    __tablename__ = 'subject_interest'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    path_video = db.Column(db.String(300))

class PersonVideo(db.Model, SerializerMixin):
    __tablename__ = 'person_video'
    id = db.Column(db.Integer, primary_key = True)
    person_name = db.Column(db.String(200))
    path_video =  db.Column(db.String(300))
