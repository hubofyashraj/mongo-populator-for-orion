import random

def create_connections_collection(database_name, client):

    
    # Select or create the database
    db = client[database_name]
    
    # Retrieve users collection
    users_collection = db['users']
    
    # Retrieve all usernames from users collection
    existing_usernames = [user['username'] for user in users_collection.find({}, {"username": 1})]
    
    # Create the collection with specified schema
    collection_name = 'connections'
    collection = db[collection_name]
    print(f"Collection '{collection_name}' with schema:")
    print("{ 'username': string, 'connections': Array<string> }")
    
    # Insert initial documents with empty connections
    documents = []
    for username in existing_usernames:
        documents.append({
            "username": username,
            "connections": []
        })
    
    # Maximum connections per user
    max_connections = len(existing_usernames) // 2
    
    # Establish connections between users
    for document in documents:
        username = document['username']
        
        # Remove current user from potential connections
        other_usernames = [user for user in existing_usernames if user != username]
        
        # Determine random number of connections, up to max_connections
        num_connections = random.randint(0, max_connections)
        connections = random.sample(other_usernames, num_connections)
        
        # Ensure bidirectional connections
        for connection in connections:
            if connection not in document['connections']:
                document['connections'].append(connection)
                # Ensure bidirectional connection for the other user as well
                other_user_document = next((doc for doc in documents if doc['username'] == connection), None)
                if other_user_document and username not in other_user_document['connections']:
                    other_user_document['connections'].append(username)
    
    # Insert documents with established connections
    collection.insert_many(documents)
    
    print(f"{len(documents)} documents inserted into '{collection_name}'.")

