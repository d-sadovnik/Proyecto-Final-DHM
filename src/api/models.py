from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "t_user"
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
    __tablename__="t_ejercicios"
    ejercicioid = db.Column(db.Integer, primary_key=True)
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
    __tablename__= "t_musculos"
    musculoid = db.Column(db.Integer, primary_key=True)
    musculo = db.Column(db.String(120), unique=True ,nullable=False)

    def __repr__(self):
        return f'<Musculo {self.musculo}'
    
    def serialize(self):
        return { 
            "id": self.musculoid,
            #"id_grupo_muscular": self.grupomuscularid,
            "musculo": self.musculo,
        }

class GrupoMuscular(db.Model):
    __tablename__= "t_grupo_muscular"
    grupomuscularid = db.Column(db.Integer,primary_key=True)
    #""" rutinapredeterminadaid = db.Column(db.Integer, db.ForeignKey("t_rutina_predeterminada.rutinapredeterminadaid")) """
    grupo_nombre = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Grupo Muscular {self.grupo_nombre}'
    
    def serialize(self):
        return { 
            "id": self.id,
            "rutina_predeterminada": self.rutinapredeterminadaid,
            "grupo_nombre": self.grupo_nombre,
        }

class RutinaLibre(db.Model):
    __tablename__= "t_rutina_libre"
    rutinalibreid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    #""" rutinadeldiaid = db.relationship("t_rutina_del_dia", back_populates="rutinalibre", uselist=False) """

    def __repr__(self):
        return f'< Rutina Libre {self.name}'
    
    def serialize(self):
        return {
            "rutinalibreid": self.rutinalibreid,
            "musculoid": self.musculoid,
            "rutina_libre_nombre": self.name,
        }

class Rutina_del_dia(db.Model):
    __tablename__= "t_rutina_del_dia"
    rutinadeldiaid =  db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("t_user.id"))
    #"""rutinapredeterminadaid = db.Column(db.Integer, db.ForeignKey("t_rutina_predeterminada.rutinapredeterminadaid"), nullable=True)
    #rutinalibreid = db.Column(db.Integer, db.ForeignKey("t_rutina_libre.rutinalibreid"), nullable=True)

    def __repr__(self):
        return f'<Rutina del dia {self.rutinadeldiaid}'

    def serialize(self):
        return {
            "rutinadeldiaid": self.rutinadeldiaid,
            "userid": self.userid,
            "rutinapredeterminadaid": self.rutinapredeterminadaid,
            "rutinalibreid": self.rutinalibreid,
        }

class RutinaPredeterminada(db.Model):
    __tablename__= "t_rutina_predeterminada"
    rutinapredeterminadaid= db.Column(db.Integer, primary_key=True)
    #""" rutinadeldiaid = db.Column(db.Integer, db.ForeignKey("t_rutina_del_dia.rutinadeldiaid")) """
    nombrerutina= db.Column(db.String(120), nullable=False)
    #""" rutinadeldia = db.relationship("t_rutina_del_dia", back_populates="t_rutina_predeterminada", uselist=False) """

    def __repr__(self):
        return f'<Rutina predetermiada {self.nombrerutina}'
    
    def serialize(self):
        return {
            "rutinapredeterminadaid": self.rutinapredeterminadaid,
            "nombrerutina": self.rutinapredeterminadaid,
        }

class Tracker(db.Model):
    __tablename__= "t_tracker"
    trackerid =  db.Column(db.Integer, primary_key=True)
    #""" userID = db.Column(db.Integer, primary_key=True)
    #rutina_del_dia = db.Column(db.Integer, primary_key=True)
    #calorias_quemadas = db.Column(db.Float,nullable=False)
    #distancia_recorrida = db.Column(db.Float,nullable=False)
    #pasos_diarios = db.Column(db.Float,nullable=False) """

    def __repr__(self):
        return f'<Tracker {self.distancia_recorrida} km'
    
    def serialize(self):
        return {
            "trackerid":self.trackerid,
            "calorias_quemadas":self.calorias_quemadas,
            "distancia_recorrida":self.distancia_recorrida,
            "pasos_diarios":self.pasos_diarios,
        }

class Profile(db.Model):
    __tablename__= "t_profile"
    profileid = db.Column(db.Integer, primary_key=True)
    #userid = db.Column(db.Integer, primary_key=True)
    edad = db.Column(db.Integer, nullable=False)
    altura = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    masa_muscular = db.Column(db.Integer, nullable=False)
    grasa_corporal = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Profile {self.userid}'

    def serialize(self):
        return {
            "profileid":self.profileid,
            "edad":self.edad,
            "altura":self.altura,
            "peso":self.peso,
            "masa_muscular":self.masa_muscular,
            "grasa_corporal":self.grasa_corporal,
        }





