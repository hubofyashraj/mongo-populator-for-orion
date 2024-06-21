def populate_user_stats_collection(database_name, client):

    # Select or create the database
    db = client[database_name]
    
    # Retrieve users collection
    users_collection = db['users']
    
    # Retrieve connections collection
    connections_collection = db['connections']
    
    # Initialize an empty list to store user_stats documents
    user_stats_documents = []
    
    # Iterate over users from users collection
    for user in users_collection.find():
        # Find connections document for the current user
        connections_document = connections_collection.find_one({"username": user['username']})
        
        # Calculate connections count (length of connections array)
        if connections_document and 'connections' in connections_document:
            connections_count = len(connections_document['connections'])
        else:
            connections_count = 0
        
        # Create user_stats document
        user_stats_document = {
            "username": user['username'],
            "postsCount": 0,  # Assuming postsCount starts at 0
            "connectionsCount": connections_count
        }
        
        # Append user_stats document to the list
        user_stats_documents.append(user_stats_document)
    
    # Insert user_stats documents into user_stats collection
    if user_stats_documents:
        user_stats_collection = db['user_stats']
        result = user_stats_collection.insert_many(user_stats_documents)
        print(f"{len(result.inserted_ids)} documents inserted into 'user_stats' collection.")
    else:
        print("No documents inserted into 'user_stats' collection.")

if __name__ == "__main__":
    # Ask for the database name
    database_name = input("Enter the database name: ")

    populate_user_stats_collection(database_name)
