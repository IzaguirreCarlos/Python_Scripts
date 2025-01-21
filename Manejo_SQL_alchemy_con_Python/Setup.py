from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# URL DE LA  BASE DE DATOS
DATABASE_PASSWORD = os.getenv("DATA_PASSWORD")
DATABASE_URL = f"mysql+pymysql://carlos:{DATABASE_PASSWORD}@localhost:3306/Data_Base_ALFHA_25"

# CREAR EL MOTOR DE LA BASE DE DATOS
motor = create_engine(DATABASE_URL, echo=True)

# Clase base para definir los modelos
base = declarative_base()
# Configuracion del inicio de Sesion
session = sessionmaker(bind=motor)
# Abrir la sesion
session = session()

# Definicion de un Modelo
class User(base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# CREAR TABLA

try:
    base.metadata.create_all(motor)
    print("Base de Datos y Tabla Creada Exitosamente::")
except:
    print("No se Pudo Crear la Base de Datos")


