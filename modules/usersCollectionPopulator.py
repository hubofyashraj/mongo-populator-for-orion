from faker import Faker
import bcrypt

# Initialize Faker generator
fake = Faker()

# Function to generate a hashed password
def generate_hashed_password():
    password = 'Raj'  # Constant password to be hashed
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hash the password
    return hashed.decode('utf-8')  # Return the hashed password as a string

def create_collection(database_name, client):
    
    # Select or create the database
    db = client[database_name]
    
    # Define the schema
    schema = {
        "username": "username",
        "fullname": "name",
        "password": generate_hashed_password()
    }
    
    # Ask for the number of documents
    while True:
        try:
            num_documents = int(input("Enter number of documents to insert: "))
            if num_documents > 0:
                break
            else:
                print("Number of documents must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Create the collection with specified schema
    collection_name = 'users'
    collection = db[collection_name]
    print(f"Collection '{collection_name}' with schema:")
    print(schema)
    
    # Insert documents
    documents = []
    for _ in range(num_documents):
        document = {
            "username": fake.user_name(),
            "fullname": fake.name(),
            "password": schema["password"]
        }
        documents.append(document)
    
    collection.insert_many(documents)
    
    print(f"{num_documents} documents inserted into '{collection_name}'.")

