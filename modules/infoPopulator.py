from faker import Faker

# Initialize Faker generator
fake = Faker()

def populate_info_collection(database_name, client):
    
    # Select or create the database
    db = client[database_name]
    
    # Retrieve users collection
    users_collection = db['users']
    
    # Retrieve all users from users collection
    users = users_collection.find({})
    
    # Create the collection with specified schema
    collection_name = 'info'
    collection = db[collection_name]
    print(f"Collection '{collection_name}' with schema:")
    print("{ 'username': string, 'fullname': string, 'dob': string, 'profession': string, "
          "'location': string, 'bio': string, 'gender': string, 'email': string, "
          "'contact': string, 'contact_privacy': boolean, 'pfp_uploaded': boolean }")
    
    # Insert documents into 'info' collection
    documents = []
    for user in users:
        info_document = {
            "username": user['username'],
            "fullname": user['fullname'],
            "dob": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
            "profession": fake.job(),
            "location": fake.city(),
            "bio": fake.text(max_nb_chars=200),
            "gender": fake.random_element(elements=('Male', 'Female', 'Other')),
            "email": fake.email(),
            "contact": fake.phone_number(),
            "contact_privacy": False,
            "pfp_uploaded": False
        }
        documents.append(info_document)
    
    # Insert all documents into 'info' collection
    collection.insert_many(documents)
    
    print(f"{len(documents)} documents inserted into '{collection_name}'.")

if __name__ == "__main__":
    # Ask for the database name
    database_name = input("Enter the database name: ")

    populate_info_collection(database_name)
