from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
            # do not serialize the password, its a security breach
        }
class People(db.Model):
    __tablename__ = 'people'
    id  = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    homeworld = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass" : self.mass,
            "hair_color" : self.hair_color,
            "skin_color" : self.skin_color,
            "eye_color" : self.eye_color,
            "birth_year" : self.birth_year,
            "gender" : self.gender,
            "created" : self.created,
            "edited" : self.edited,
            "homeworld" : self.homeworld,
            "url" : self.url
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter= db.Column(db.Integer, nullable=False)
    rotation_period= db.Column(db.Integer, nullable=False)
    orbital_period= db.Column(db.Integer, nullable=False)
    gravity= db.Column(db.String(50), nullable=False)
    population= db.Column(db.Integer, nullable=False)
    climate= db.Column(db.String(50), nullable=False)
    terrain= db.Column(db.String(50), nullable=False)
    surface_water= db.Column(db.Integer, nullable=False)
    created= db.Column(db.DateTime, nullable=False)
    edited= db.Column(db.DateTime, nullable=False)
    url= db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter":self.diameter,
            "rotation_period":self.rotation_period,
            "orbital_period":self.orbital_period,
            "gravity":self.gravity,
            "population":self.population,
            "climate":self.climate,
            "terrain":self.terrain,
            "surface_water":self.surface_water,
            "created":self.created,
            "edited":self.edited,
            "url":self.url
        }

class Favorites(db.Model):
    __tablename__ = 'favorite'
    id= db.Column(db.Integer, primary_key=True)
    idpeople = db.Column(db.Integer, db.ForeignKey('people.id'))
    people = db.relationship(People, foreign_keys=[idpeople])
    iduser = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User, foreign_keys=[iduser])
    idplanet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship(Planets, foreign_keys=[idplanet])
    
    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "idpeople": self.idpeople,
            "iduser": self.iduser,
            "idplanet": self.idplanet
        }