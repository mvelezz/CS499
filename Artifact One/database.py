import urllib

from pymongo import MongoClient
from pymongo.server_api import ServerApi



def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo

    username = urllib.parse.quote_plus('miahvelez')
    password = urllib.parse.quote_plus('Password1')
    CONNECTION_STRING = "mongodb+srv://"+username+":" + password + "@cluster0.dpolx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Create a new client and connect to the server
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['CCmembers']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()