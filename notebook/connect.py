from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
MONGO_URI_ATLAS = os.getenv("MONGO_URI_ATLAS")
DATABASE_NAME = os.getenv("MONGO_DB_DATA")

try:
    client = MongoClient(MONGO_URI_ATLAS)
    print("Cliente de MongoDB Atlas creado exitosamente.")
    db = client[DATABASE_NAME]
    # # crear la base de datos en mongoDB atlas, para ello tenemos que crear una coleccion
    # db.create_collection("mi_coleccion")
    print("Conexión exitosa a la base de datos MongoDB Atlas:", DATABASE_NAME)
    print("bases de datos disponibles:", client.list_database_names())

    db.list_collection_names()
    print("Conectado Atlas, Base de datos:", DATABASE_NAME)
    print("Colecciones disponibles:", db.list_collection_names()) 


except errors.ServerSelectionTimeoutError as e:
    print("Error de conexión a MongoDB Atlas:", e)
except errors.OperationFailure as e:
    print("Error de autenticacion:", e)