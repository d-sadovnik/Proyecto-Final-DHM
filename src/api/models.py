from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            # do not serialize the password, its a security breach
        }

class Ejercicios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    musculoid = db.Column(db.Integer)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<Ejercicio {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "musculoid": self.musculoid,
            "name": self.name,
            "description": self.description,
        }

class Musculos(db.Model):
    musculoid = db.Column(db.Integer,primary_key=True)
    grupomuscularid = db.Column(db.Integer,primary_key=True)
    musculo = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Musculo {self.musculo}'
    
    def serialize(self):
        return { 
            "id": self.musculoid,
            "id_grupo_muscular": self.grupomuscularid,
            "musculo": self.musculo,
        }

class Grupo_muscular(db.Model):
    grupomuscularid = db.Column(db.Integer,primary_key=True)
    rutinapredeterminadaid = db.Column(db.Integer,primary_key=True)
    grupo_nombre = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Grupo Muscular {self.grupo_nombre}'
    
    def serialize(self):
        return { 
            "id": self.id,
            "rutina_predeterminada": self.rutinapredeterminadaid,
            "grupo_nombre": self.grupo_nombre,
        }

class Rutina_libre(db.Model):
    rutinalibreid = db.Column(db.Integer, primary_key=True)
    musculoid = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'< Rutina Libre {self.name}'
    
    def serialize(self):
        return {
            "rutinalibreid": self.rutinalibreid,
            "musculoid": self.musculoid,
            "rutina_libre_nombre": self.name,
        }

class Rutina_del_dia(db.Model):
    rutinadeldiaid =  db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    rutinapredeterminadaid = db.Column(db.Integer,primary_key=True)
    rutinalibreid = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<Rutina del dia {'