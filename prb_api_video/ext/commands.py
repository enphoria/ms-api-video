import click

from prb_api_video.ext.auth import create_user
from prb_api_video.ext.database import db
from prb_api_video.models import Person
from prb_api_video.models import SubjectInterest
from prb_api_video.models import PersonVideo


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    print("Populate db with sample data")
    data = [
        SubjectInterest(id=1, name="Seguridad", path_video="./././video/iniciative/Seguridad.mp4"),
        SubjectInterest(id=2, name="Educacion", path_video="./././video/iniciative/Educacion.mp4"),
        PersonVideo(id=1, person_name="Sergio", path_video="./././video/name/Sergio.mp4"),
        PersonVideo(id=2, person_name="Carlos", path_video="./././video/name/Carlos.mp4"),
        PersonVideo(id=3, person_name="Luis", path_video="./././video/name/Luis.mp4"),
        PersonVideo(id=4, person_name="Camilo", path_video="./././video/name/Camilo.mp4"),
        PersonVideo(id=5, person_name="Viviana", path_video="./././video/name/Viviana.mp4"),
        PersonVideo(id=6, person_name="Jorge", path_video="./././video/name/Jorge.mp4"),
        PersonVideo(id=7, person_name="Angela", path_video="./././video/name/Angela.mp4"),
        Person(id=1, name="Sergio", lastname="Fajardo", cellphone=3128348183, city="Bogota", locality="Barrios Unidos", subject_interest_id=1, person_video_id=1),
        Person(id=2, name="Carlos", lastname="Macana", cellphone=3222674989, city="Bogota", locality="Chapinero", subject_interest_id=2, person_video_id=2),
        Person(id=3, name="Luis", lastname="Carrillo", cellphone=3195032885, city="Bogota", locality="Bosa", subject_interest_id=1, person_video_id=3),
        Person(id=4, name="Camilo", lastname="Cardenas", cellphone=3148621961, city="Bogota", locality="Kennedy", subject_interest_id=2, person_video_id=4),
        Person(id=5, name="Viviana", lastname="Barbena", cellphone=3208601369, city="Bogota", locality="Martires", subject_interest_id=1, person_video_id=5),
        Person(id=6, name="Jorge", lastname="Torres", cellphone=3127455593, city="Bogota", locality="Engativa", subject_interest_id=1, person_video_id=6),
        Person(id=7, name="Angela", lastname="Hurtado", cellphone=451961237, city="Bogota", locality="Ciudad Bolivar", subject_interest_id=2, person_video_id=7),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Person.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option("--username", "-u")
    @click.option("--password", "-p")
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
