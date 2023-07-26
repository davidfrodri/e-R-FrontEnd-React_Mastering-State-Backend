from pymongo import MongoClient

mongo_url = "mongodb+srv://davidfrodri:contrasena@e-big-comunity.pyc74u1.mongodb.net/"

db_client = MongoClient(mongo_url)

employers_database = db_client['e-employers']
subscribers_database = db_client['e-subscribe-emails']