from app import db


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    address = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120), nullable = False)
    genres = db.Column(db.String(120), nullable = False)
    image_link = db.Column(db.String(500), nullable = False)
    facebook_link = db.Column(db.String(120))
    web_link = db.Column(db.String(120))
    look_for_talent = db.Column(db.Boolean, nullable = False,
                                default = False)
    talent_description = db.Column(db.String())


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    city = db.Column(db.String(120), nullable = False)
    state = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(120), nullable = False)
    genres = db.Column(db.String(120), nullable = False)
    image_link = db.Column(db.String(500), nullable = False)
    facebook_link = db.Column(db.String(120), nullable = True)
    web_link = db.Column(db.String(120))
    look_for_venue = db.Column(db.Boolean, nullable = False,
                                default = False)
    Venue_description = db.Column(db.String())
