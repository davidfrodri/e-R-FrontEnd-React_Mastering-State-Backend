from pymongo import MongoClient

mongo_url = "mongodb+srv://davidfrodri:contrasena@e-big-comunity.pyc74u1.mongodb.net/"

db_client = MongoClient(mongo_url)

my_database = db_client['e-employers']