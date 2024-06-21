from pymongo import MongoClient
from modules.connectionsPopulator import create_connections_collection
from modules.infoPopulator import populate_info_collection
from modules.user_statsPopulator import populate_user_stats_collection
from modules.usersCollectionPopulator import create_collection

# Ask for the database name
database_name = input("Enter the database name: ")
mongo_uri = input("Enter mongodb uri: ")
# Connect to MongoDB
client = MongoClient(mongo_uri)


if __name__=='__main__':
    # Populating users credentials 
    create_collection(database_name, client)

    # Populating user info
    populate_info_collection(database_name, client)

    # Populating connections collection 
    create_connections_collection(database_name, client)

    # Populating user stats
    populate_user_stats_collection(database_name, client)


