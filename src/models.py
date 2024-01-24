import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    fechadenacimiento = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fechadesuscripcion = Column(String(250), nullable=False)
    contrasena = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    poblacion = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    idioma = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)
    oxigeno = Column(String(250), nullable=False)
    creado = Column(String(250), nullable=False)
    localizacion = Column(String(250), nullable=False)
    gobernante = Column(String(250), nullable=False)
    Residentes = Column(String(250), nullable=False)
    Soles = Column(String(250), nullable=False)
    lunas = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    fechadenacimiento = Column(String(250), nullable=False)
    home = Column(String(250), nullable=False)
    raza = Column(String(250), nullable=False)
    padres = Column(String(250), nullable=False)
    conyugue = Column(String(250), nullable=False)
    hijos = Column(String(250), nullable=False)
    ocupacion = Column(String(250), nullable=False)
    titulo = Column(String(250), nullable=False)
    equipamiento = Column(String(250), nullable=False)
    enemigos = Column(String(250), nullable=False)
    afiliaciones = Column(String(250), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Favorites(Base):
    __tablename__ = 'favorites'
    user = relationship (User)
    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
